import argparse
import yaml
import os
import pandas as pd
from src.data_utils.rain_loader import load_rain_to_df

def parse_config(path):
    with open(path, 'r') as f:
        return yaml.safe_load(f)

def main():
    parser = argparse.ArgumentParser(description="Run rain extraction for a basin")
    parser.add_argument('--config', type=str, required=True, help='Path to YAML config file')
    args = parser.parse_args()

    config = parse_config(args.config)

    df = load_rain_to_df(
        nc_path=config['rain_file'],
        basin_name=config['basin_name'],
        basins_path=config['basins_layer'],
        chunk_size=config.get('chunk_size', 500),
        device=config['device']
    )

    os.makedirs(os.path.dirname(config['output_path']), exist_ok=True)
    df.to_csv(config['output_path'], index=False)
    print(f"✅ Saved output to {config['output_path']}")

if __name__ == "__main__":
    main()

