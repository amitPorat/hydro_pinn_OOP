import yaml
from UGRID_builder import UGRIDBuilder
from pathlib import Path


def load_config(config_path):
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)
    return config


def main():
    config_path = Path(__file__).parent / "config.yaml"
    config = load_config(config_path)

    # Set output directory to artifacts
    output_dir = Path(__file__).parent.parent.parent / "artifacts"
    output_dir.mkdir(exist_ok=True)  # Ensure it exists

    print("[•] Initializing UGRIDBuilder...")
    builder = UGRIDBuilder(config, output_dir=output_dir)  # Pass output_dir

    print("[•] Running process...")
    builder.run()


if __name__ == "__main__":
    main()
