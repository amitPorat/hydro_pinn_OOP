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
