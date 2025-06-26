# 📊 Project Data Documentation

This file documents the key datasets used in the `hydro_pinn_OOP` project. Keeping this updated is part of the team standard.

## 1. Basins Layer – `data/basins/Basins_Web_V13.*`
- **Type:** Shapefile (`.shp`, `.dbf`, `.shx`, `.prj`, `.cpg`)
- **Purpose:** National watershed boundaries of Israel
- **Used by:** `src/data_utils/basin_utils.py → get_basin_bounds()`
- **Key field:** `NAME_EN` – used to match basin from config
- **Example basins:** `Darga`, `Arugot`, `Khatsatson`
- **Used in:** `example_config.yaml → basins_layer`

## 2. Rainfall Files – `data/rain/RMYYYY.nc`
- **Format:** NetCDF (`netCDF4.Dataset` or `xarray.Dataset`)
- **Variable:** `RAINRATE`
- **Grid Variables:** `rlat`, `rlon`
- **Time Axis:** `time`, with units like `"minutes since YYYY-MM-DD"`
- **Usage:** Loaded in `rain_loader.py`, sliced by basin bounds
- **Size:** Large (do not push full files to GitHub)

## 3. Flow Data – CSV
- **Files:** Not committed to GitHub (used locally)
- **Fields:** `date`, `rg_qms`, `name` (station name), etc.
- **Used for:** Merging with rain, training PINN
- **Lag:** In some experiments, rain shifted 3 hours to match Q

## 4. Outputs – `outputs/` folder
- CSV files saved per basin/year
- Animated maps saved as `.html`

## 🔁 Version Tracking Reminder
- Always update this file when:
  - Adding a new data source
  - Changing a file path or format
  - Updating field names
- Keep `README.md`, `DATA.md`, and `config/` **in sync**

---

This file is meant to keep everyone aligned — especially as the project moves toward production and new contributors/servers get involved.