# UGRID Builder – Full Project Documentation

This document describes the logic, structure, and usage of the `UGRID_builder` module, which creates a variable-resolution unstructured grid (UGRID) from a high-resolution DEM without relying on an external stream shapefile. The process automatically detects stream-like features and assigns physical equations based on spatial characteristics.

---

## 📌 Purpose

The goal is to create a high-resolution hydrological mesh that:
- Uses only a DEM and a basin shapefile as input.
- Derives streams using flow accumulation.
- Builds a **quadtree-based variable resolution grid**:
  - High resolution around streams.
  - Coarser resolution elsewhere.
- Assigns **governing equations** to each grid cell (e.g., SWE, KWE, SCS).

---

## 📁 Folder Structure

```
UGRID_builder/
├── builder.py          # UGRIDBuilder class – main controller
├── flow_tools.py       # Flow accumulation, direction, and stream extraction (WhiteboxTools)
├── quadtree.py         # Recursive quadtree generation and resolution classification
├── utils.py            # Clipping, raster-to-point, export helpers
├── main.py             # Entry point script
├── config.yaml         # User configuration
├── __init__.py         # Declares package structure
├── data/               # Input DEM + basins
└── output/             # Output shapefiles, rasters, and CSVs
```

---

## 🧠 Core Algorithm Steps

### 1. Load Input Data
- Read `dem.tif` and `basins.shp`.
- Select the basin polygon by name (`NAME_EN` field).

### 2. Clip DEM to Basin
- DEM is spatially masked to the basin polygon using `rasterio.mask`.

### 3. Compute Hydrological Layers
Using **WhiteboxTools**:
- `d8_pointer`: calculates flow direction raster.
- `d8_flow_accumulation`: generates a flow accumulation raster.
- `extract_streams`: identifies stream cells where accumulation > threshold.

### 4. Convert Stream Raster to Points
- All raster cells marked as streams are converted to `shapely.geometry.Point` objects.

### 5. Build Quadtree Grid
- A recursive subdivision algorithm (`quad_subdivide`) splits the basin bounding box into quadrants based on point density.
- Subdivision continues until:
  - Number of points in box ≤ threshold, or
  - Max recursion depth is reached.
- Final bounding boxes are converted to polygons and clipped to the basin geometry.

### 6. Classify Grid Cell Resolution
- Grid cells are categorized by area:
  - Lowest 25% → `high` resolution
  - Middle 50% → `medium` resolution
  - Largest 25% → `low` resolution

### 7. Assign Physical Equations
Based on resolution:
- `high` → SWE (Shallow Water Equations)
- `medium` → KWE (Kinematic Wave Equation)
- `low` → SCS (Curve Number / empirical)

### 8. Export Results
- Grid cells (as polygons) are saved to:
  - Shapefile `.shp`
  - CSV `.csv` with attributes (`ID`, `area`, `equation`, etc.)

---

## ⚙️ config.yaml Example

```yaml
basin_name: Darga
stream_threshold: 500

paths:
  dem: data/dem.tif
  basins: data/basins.shp
  output_dir: output/
```

---

## ▶️ Running the Code

From inside `UGRID_builder/`:
```bash
python main.py
```

From outside (e.g., project root):
```bash
python -m UGRID_builder.main
```

---

## ✅ Requirements

- Python ≥ 3.8
- Libraries:
  - `geopandas`, `rasterio`, `shapely`, `numpy`, `pandas`, `PyYAML`
  - `whitebox` (install via: `pip install whitebox`)

---

## 📌 Notes

- DEM must be in projected coordinates (e.g., EPSG:2039).
- Resolution-aware: works well with 4-meter DEM.
- Stream detection is fully automatic using flow accumulation.
- Suitable for hybrid physics-informed ML workflows (e.g., PINNs).

