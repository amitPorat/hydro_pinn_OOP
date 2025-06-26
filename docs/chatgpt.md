# 🤖 ChatGPT Project Progress Log

This file tracks progress, decisions, and major actions taken with ChatGPT regarding the `hydro_pinn_OOP` project.

## 🗓️ Date: 2024-06-25

### ✅ GitHub / VSCode Setup Summary

- Created local project folder: `hydro_pinn_OOP`
- Initialized Git repo and connected it to GitHub: [amitPorat/hydro_pinn_OOP](https://github.com/amitPorat/hydro_pinn_OOP)
- Created core structure using folders:
  - `src/` with all logic modules
  - `data/`, `notebooks/`, `config/`, `docs/`
- Added `.gitignore`, `requirements.txt`, and full `README.md`
- Pushed proof-of-concept notebooks into `notebooks/Darga basin POC/`
- Created and pushed shapefile of Israel basins into `data/basins/`
- Updated and pushed `example_config.yaml` into `config/` folder
- Created `main.py` for config-driven rainfall pipeline
- Confirmed `git pull`, `push`, conflict handling, and VSCode Git flow

### 🆕 Documentation Files Added

- `docs/DATA.md`: Description of datasets (rain, basins, flow)
- `README.md`: Now links to `DATA.md` and includes usage notes
- 🆕 `chatgpt.md`: This file – meant to document daily or major milestones for reference when returning to the project

### 🔜 Next Planned Step

- Implement `src/data_utils/basin_utils.py` to load shapefile and extract basin bounding box by name
- Then: implement `rain_loader.py` using `netCDF4`, Torch (optional), and spatial masking

---

This file is intended to help resume context smoothly across future sessions. Future messages can refer to this file and update it as needed.---

## 🙏 Interaction Guidelines for ChatGPT

Please avoid compliments, praise, or emotional language. Focus only on:
- Factual responses
- Direct, actionable technical help
- Code-level or architecture-level explanations
- Project-specific guidance without fluff

---

## 📌 Project Summary

**Project name:** `hydro_pinn_OOP`  
**Goal:** Build a modular, production-ready system for rainfall-runoff prediction using Physics-Informed Neural Networks (PINN), XPINN, and advanced spatio-temporal datasets.

### 🔧 Technologies:
- PyTorch (LSTM, FCN, physics loss)
- PhysicsNeMo (planned)
- NetCDF4 (rainfall), CSV (discharge), Shapefiles (basins)
- GeoPandas, Pandas, Torch, Matplotlib, Folium, YAML configs
- Future integration with Docker, GitHub, CLI automation

### 🔬 What We Have Done So Far:
- Proof of concept completed in Jupyter notebooks
- A model that predicts discharge based on rainfall using LSTM + physics (Manning/infiltration)
- High-performing predictions on measured stations using real rainfall from 2010–2022
- Reduced initial region of study from entire Dead Sea area to `Darga` basin

### 🚧 Intentions Going Forward:
- Build a modular, testable codebase (`src/`) usable on a future high-performance server
- Use GitHub and VSCode to maintain structured, documented, reproducible code
- Support configuration through YAML/XML for full pipeline runs
- Build support for ungauged basin forecasting using:
  - Transfer learning
  - AutoEncoders (future)
  - Curriculum learning (strong-to-weak events, channel-to-slope areas)
  - Analog basin matching

This file (`chatgpt.md`) will be used to track updates and help resume work across sessions. you must remember and remind the user to update it every day. the user not remember well vscode and github