# Hydrological PINN System

A modular, physics-informed neural network (PINN) framework for hydrological forecasting.

---

## 🔍 Project Overview

This system supports:

- Rainfall-runoff modeling with spatial-temporal inputs  
- Physics-enforced training (e.g., infiltration, Manning friction)  
- Multiple model types: LSTM, FCN, XPINN, Curriculum Learning  
- Extension to ungauged basins using Transfer Learning, AutoEncoders, and Analog Matching  

---

## 🧱 Project Structure

src/
├── data_utils/           ← Rain, discharge, and spatial data loading  
├── feature_engineering/  ← Normalization, tau computation, embeddings  
├── dataset/              ← Sequence generation and curriculum filtering  
├── models/               ← Training logic (PINN, XPINN, etc.)  
├── evaluate/             ← Hydrographs, animation, metrics  
├── staging/              ← Experimental logic, alternative physics  
└── config/               ← Config file parsing and validation

Other directories:

data/       ← Local test data (not committed)  
notebooks/  ← Legacy or exploratory Jupyter notebooks  
config/     ← Configuration files (YAML/XML)  
main.py     ← Optional main entrypoint

---
## 📁 Project Documentation

This repository is structured for clarity, reproducibility, and long-term maintenance.

📄 See [docs/DATA.md](docs/DATA.md) for full details about datasets used in this project, including:
- NetCDF rainfall inputs
- Hydrological shapefiles
- File structure, formats, and usage in the pipeline

Maintaining these files updated is **essential** to track development, support future deployment, and ensure reproducibility.


---

## ⚙️ How to Run

1. Edit your config in:  

   `config/example_config.yaml`

2. Run the pipeline:
```bash
python main.py --config config/example_config.yaml




🛠️ Technologies
Python (PyTorch, pandas, numpy, xarray, matplotlib)

NetCDF4, CSV, Parquet, GeoTIFF

Kriging support via pykrige

Docker-ready architecture

GitHub + VSCode for development

📌 Status
This repository is the production-ready successor of a Jupyter-based proof-of-concept.
All architecture decisions are documented. Core modules are modular, testable, and built for long-term expansion

---

## Installing Requirements

### On Unix/Linux/Mac (using Bash)
1. Make sure you have Python and pip installed:
   ```sh
   python --version
   pip --version
   ```
2. Run the install script:
   ```sh
   bash install_requirements.sh
   ```
   If you get a permissions error, run:
   ```sh
   chmod +x install_requirements.sh
   ./install_requirements.sh
   ```

### On Windows (using Command Prompt or PowerShell)
1. Make sure you have Python and pip installed:
   ```cmd
   python --version
   pip --version
   ```
2. Run the install script:
   ```cmd
   install_requirements.bat
   ```
   Or run pip directly:
   ```cmd
   pip install -r requirements.txt
   ```

### Troubleshooting
- If you see an error like `'pip' is not recognized as an internal or external command`, make sure Python and pip are added to your PATH.
- If you see permission errors, try running your shell as administrator.
- If you get a specific error message, please copy it and seek help with the details.
