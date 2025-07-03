# chatgpt_final.md – Combined Project Documentation

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


## 🐳 Docker and Environment Setup (New)

- Created a `Dockerfile` for the project (supports CPU/GPU runtime)
- Added `requirements.txt` with all Python dependencies
- Both files added to project root and tested in local VSCode
- `docker build` and `docker run` work end-to-end with config-based execution
- These files are version-controlled and compatible with deployment pipeline

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

---

# chatgpt.md – Project Development Log for `hydro_pinn_OOP`

This document tracks the evolution, key milestones, architectural shifts, and design choices in the hydrological PINN-based flood prediction system (`hydro_pinn_OOP`). It combines insights from code notebooks, planning documents (Sprint Manifest, Work Plan 2.0), and observed experimental phases.

---

## 🧪 Phase 1: Initial Proof of Concept (POC) – Small-Scale

- **Timeframe:** Early development
- **Focus Area:** North Dead Sea
- **Years Covered:** 2012–2013
- **Structure:**
  - Used full timestep data → ~13M rows/year
  - Basic features: rainfall, elevation, slope (with many NaNs), rg_qms
  - Model: basic NN, no physics
- **Problems:**
  - Very large datasets caused memory overload
  - Many dry timesteps added noise and inefficiency
  - Missing slope values, weak spatial support
- **Fixes:**
  - Switched to event-based slicing (Nov–Apr, discharge threshold)
  - Reduced data by >10×
  - Added Tau (normalized event time)

---

## 📈 Phase 2: Scaling the POC – More Years & Data Cleanup

- **Years Added:** 2014–2016, 2018–2020
- **Challenges:**
  - Inconsistent time indexing per year (Tau reset per year)
  - Missing values in slope_calculated
- **Fixes:**
  - Global timestamp normalization across all years (Global Tau)
  - Filled missing slope values (e.g. mean imputation)
  - Event-based filtering extended to all years

---

## 🌐 Phase 3: Spatial Data Enrichment (UGRID)

- **Static Dataset Added:** UGRID (DEM-derived + hydro features)
- **Features Added:**
  - Area, slope, flow direction, stream order, aspect, TRI, TPI, roughness, D50, Manning n, etc.
- **Fixes:**
  - Merged with event data via grid cell ID or lat/lon
  - Verified station cells have STREAM_CELL=1 and realistic area values
  - Replaced slope_calculated with UGRID’s complete slope where needed

---

## 🚀 Phase 4: Pipeline Efficiency & Parquet Conversion

- **Problems:**
  - CSVs were slow and memory-heavy to load (1.6GB+/year)
  - Repeating preprocessing was time-consuming
- **Fixes:**
  - Preprocessed each year once and saved as `.parquet`
  - Unified structure with global Tau and UGRID-merged features
  - Batch loaded via list of Parquet paths (train/test)

---

## 🧠 Phase 5: Model Refinement with Physics-Informed Loss (PINN)

- **Model Structure:**
  - Input: rainfall, Tau, spatial features
  - Output: predicted discharge (log q)
- **Loss Function:**
  - `loss_total = loss_data + λ * loss_physics`
  - loss_physics split into collocation points and station residuals
- **Stability Techniques:**
  - Gradient clipping
  - Progressive training (SCS → Delta-Q → KW → SWE)
  - Epoch-based refinement

---


## 🧾 Configuration File Overhaul (2025-07-01)

- Rebuilt the core YAML configuration file (`config.yaml`) to reflect actual user choices and architecture.
- Introduced `data_selection.method` key to switch between:
  - `date_range`: conventional start/end date splits
  - `event_based`: filter by rainy season and thresholds (active mode)
- Defined clear `train`, `validation`, and `test` periods when using date-based selection.
- Added full support for physics-informed configurations with hierarchical domains:
  - `main_channel`: Shallow Water Equations (SWE)
  - `slopes`: Kinematic Wave (KW)
  - `junctions`: continuity constraint
- Included `physics.enabled`, `hierarchy_mode`, and per-domain PDE logic
- Added `loss_weights`, `early_stopping`, and full optimizer control under `training`
- Output section expanded to support saving logs, checkpoints, TensorBoard, and final model
- Designed for long-term use on future high-performance servers and automated CLI

## 🧩 Sprint Manifest – Final Phase of POC (Last Few Weeks)

- **Tasks Completed:**
  - Equation assignment per cell (SWE, KW, Delta-Q, SCS-CN)
  - Manning's n estimated per cell (SWE)
  - Kriging interpolation across quadtree resolutions (7K, 16K, 70K)
  - Data merge: rainfall + spatial + discharge
  - Tau-based formatting (6h, 12h lead time)
  - New architecture + loss function updates
  - Resolution-specific experiments (3x per resolution)
  - Gradual training transitions (physics-based)
  - Hyperparameter tuning started
- **Tools Used:** Docker, Git, VSCode

---

## 🛠️ Work Plan 2.0 (Future Vision)

- **Total Duration:** 2.5 years
- **Key Steps:**
  1. Finalize high-res POC for North Dead Sea (5–6 months)
  2. Expand to 17 additional hydro-regions across Israel
  3. Add generalization layer for ungauged areas (AutoEncoder)
  4. Deploy user-facing dashboards + professional environment
- **Target Resolutions:** 4m DEM (~34GB), nationwide scale
- **Frameworks:** PhysicsNeMo, DeepXDE

---

## ✅ Current Status Summary (June 2025)

- 90% of POC implementation complete
- Full integration of spatial + temporal + physics data
- Modular training notebook with PINN losses working
- Parquet pipeline tested and in production use
- Clear roadmap for full model deployment