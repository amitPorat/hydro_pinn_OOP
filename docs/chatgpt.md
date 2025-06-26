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

This file is intended to help resume context smoothly across future sessions. Future messages can refer to this file and update it as needed.