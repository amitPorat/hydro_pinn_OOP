import geopandas as gpd
import rasterio
from rasterio.mask import mask
from shapely.geometry import Point
import numpy as np
import pandas as pd
from pathlib import Path


def clip_raster_to_polygon(raster_path, polygon_gdf, output_path):
    with rasterio.open(raster_path) as src:
        geoms = [geom.__geo_interface__ for geom in polygon_gdf.geometry]
        out_image, out_transform = mask(src, geoms, crop=True)
        out_meta = src.meta.copy()

    out_meta.update({
        "driver": "GTiff",
        "height": out_image.shape[1],
        "width": out_image.shape[2],
        "transform": out_transform
    })

    with rasterio.open(output_path, "w", **out_meta) as dest:
        dest.write(out_image)


def raster_to_points(raster_path):
    with rasterio.open(raster_path) as src:
        band = src.read(1)
        transform = src.transform
        rows, cols = np.where(band > 0)
        coords = [src.xy(r, c) for r, c in zip(rows, cols)]

    points = gpd.GeoDataFrame(geometry=[Point(xy) for xy in coords], crs=src.crs)
    return points


def export_shapefile_csv(gdf, output_prefix):
    output_shp = Path(f"{output_prefix}.shp")
    output_csv = Path(f"{output_prefix}.csv")

    gdf.to_file(output_shp)
    df = pd.DataFrame(gdf.drop(columns="geometry"))
    df.to_csv(output_csv, index=False)
