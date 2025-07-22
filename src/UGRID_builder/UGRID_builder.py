import geopandas as gpd
from whitebox.whitebox_tools import WhiteboxTools
from pathlib import Path
import rasterio
import numpy as np
from shapely.geometry import Point

from flow_tools import compute_flow_and_streams
from quadtree import build_quadtree_from_points
from utils import clip_raster_to_polygon, raster_to_points, export_shapefile_csv

class UGRIDBuilder:
    def __init__(self, config):
        self.basin_name = config["basin_name"]
        self.accum_threshold = config.get("stream_threshold", 500)
        self.paths = config["paths"]

        self.dem_path = Path(self.paths["dem"])
        self.basins_path = Path(self.paths["basins"])
        self.output_dir = Path(self.paths["output_dir"])
        self.output_dir.mkdir(parents=True, exist_ok=True)

        self._load_data()

    def _load_data(self):
        self.basins = gpd.read_file(self.basins_path)
        self.basin = self.basins[self.basins["NAME_EN"] == self.basin_name]
        if self.basin.empty:
            raise ValueError(f"Basin '{self.basin_name}' not found in {self.basins_path}")

    def run(self):
        print("[1] Clipping DEM to basin...")
        dem_clipped = self.output_dir / "dem_clipped.tif"
        clip_raster_to_polygon(self.dem_path, self.basin, dem_clipped)

        print("[2] Computing flow direction and accumulation...")
        flow_dir, flow_acc, streams = compute_flow_and_streams(
            dem_clipped, self.output_dir, self.accum_threshold
        )

        print("[3] Converting stream raster to points...")
        stream_points = raster_to_points(streams)

        print("[4] Building QUADTREE based on stream points...")
        quadtree_gdf = build_quadtree_from_points(stream_points, self.basin)

        print("[5] Assigning equations to grid cells...")
        quadtree_gdf["equation"] = quadtree_gdf["resolution"].map({
            "high": "SWE",
            "medium": "KWE",
            "low": "SCS"
        }).fillna("SCS")

        print("[6] Exporting to SHP and CSV...")
        export_shapefile_csv(quadtree_gdf, self.output_dir / f"UGRID_{self.basin_name}")

        print("[✓] Done.")