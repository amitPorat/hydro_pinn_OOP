import geopandas as gpd
from shapely.geometry import box
import numpy as np


def quad_subdivide(points, box_coords, threshold, depth, max_depth):
    xmin, xmax, ymin, ymax = box_coords

    sub_points = points.cx[xmin:xmax, ymin:ymax]
    n = len(sub_points)

    if n <= threshold or depth >= max_depth:
        return [box(xmin, ymin, xmax, ymax)]
    else:
        xm = (xmin + xmax) / 2
        ym = (ymin + ymax) / 2

        boxes = []
        boxes += quad_subdivide(sub_points, (xmin, xm, ymin, ym), threshold, depth+1, max_depth)
        boxes += quad_subdivide(sub_points, (xm, xmax, ymin, ym), threshold, depth+1, max_depth)
        boxes += quad_subdivide(sub_points, (xmin, xm, ym, ymax), threshold, depth+1, max_depth)
        boxes += quad_subdivide(sub_points, (xm, xmax, ym, ymax), threshold, depth+1, max_depth)

        return boxes


def build_quadtree_from_points(points_gdf, basin_gdf, threshold=20, max_depth=10):
    bounds = basin_gdf.total_bounds  # xmin, ymin, xmax, ymax
    box_list = quad_subdivide(points_gdf, (bounds[0], bounds[2], bounds[1], bounds[3]), threshold, 0, max_depth)

    # הפוך את הרשימה ל־GeoDataFrame
    polys = gpd.GeoDataFrame(geometry=[g for g in box_list], crs=basin_gdf.crs)

    # גזירה לפי האגן
    clipped = gpd.overlay(polys, basin_gdf, how="intersection")

    # שיוך רזולוציה לפי גודל תא
    clipped["AREA"] = clipped.geometry.area
    q25, q75 = np.percentile(clipped["AREA"], [25, 75])

    def classify(area):
        if area <= q25:
            return "high"
        elif area <= q75:
            return "medium"
        else:
            return "low"

    clipped["resolution"] = clipped["AREA"].apply(classify)
    return clipped
