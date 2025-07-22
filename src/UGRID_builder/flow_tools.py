from whitebox.whitebox_tools import WhiteboxTools
from pathlib import Path

def compute_flow_and_streams(dem_path, output_dir, threshold=500):
    wbt = WhiteboxTools()
    wbt.set_working_dir(str(output_dir))

    dem_path = str(dem_path)
    flow_dir = str(Path(output_dir) / "flow_dir.tif")
    flow_acc = str(Path(output_dir) / "flow_acc.tif")
    streams = str(Path(output_dir) / "streams.tif")

    wbt.d8_pointer(dem_path, flow_dir)
    wbt.d8_flow_accumulation(dem_path, flow_acc, out_type="cells")
    wbt.extract_streams(flow_acc, streams, threshold)

    return flow_dir, flow_acc, streams
