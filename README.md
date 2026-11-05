# Predicting Prolonged Hospital Length of Stay Using ICU Patient Data

**Author:** Ruiyang Hu  
**Course:** BIOSTAT 707 Final Project  
**Project type:** Individual project; Project #1, Prolonged Length of Stay

## Project overview

This project aims to predict prolonged hospitalization using information recorded during the first 48 hours of ICU admission. The primary outcome is hospital length of stay >14 days among patients who survived hospitalization. A sensitivity analysis will examine in-hospital death or length of stay >14 days among all eligible stays. Exactly 14 days will be classified as a negative outcome.

The recorded length of stay measures time from ICU admission to the end of hospitalization, including time after ICU discharge. It does not represent ICU duration, time before ICU admission, or remaining days after the 48-hour prediction point. The study design is described in [707-proposal.md](707-proposal.md).

## Current status

Data exploration and initial outcome definitions have been completed in [notebooks/01_data_exploration.ipynb](notebooks/01_data_exploration.ipynb). Saved notebook outputs documented the following:

| Inspection result | Count |
| --- | ---: |
| Patient files and unique outcome records | 4,000 each |
| Duplicate or unmatched identifiers | 0 |
| Records excluded for missing length of stay | 60 |
| Eligible ICU stays | 3,940 |
| Eligible hospital survivors | 3,386 |
| Prolonged stays among eligible survivors | 1,025 (30.3%) |
| Death or prolonged stay among all eligible stays | 1,579 (40.1%) |

Some plotting and missingness cells have no saved outputs and require execution to display their results. Local reinspection using the notebook's rules identified substantial predictor missingness and one survivor with a recorded one-day stay, inconsistent with the documented minimum ICU duration. This timing discrepancy will require review before modeling; the counts above retain the notebook's eligibility definition.

Feature aggregation, imputation, model training, and performance evaluation have not been completed. Planned models are a simple baseline logistic regression, ridge logistic regression, and random forest. Validation will use an outcome-stratified training/test split with cross-validation restricted to training data. Learned preprocessing, including median imputation, will be fitted within training folds. Planned evaluation will include AUROC, Brier score, calibration, and appropriate comparisons of predictor importance across outcome definitions.

## Data source and license

The project uses only **Set A** of the [PhysioNet/Computing in Cardiology Challenge 2012, version 1.0.0](https://physionet.org/content/challenge-2012/1.0.0/). The source describes adult ICU stays lasting at least 48 hours, admission descriptors, first-48-hour clinical measurements, and separate hospital outcomes.

The original source files are [set-a.zip](https://physionet.org/files/challenge-2012/1.0.0/set-a.zip) and [Outcomes-a.txt](https://physionet.org/files/challenge-2012/1.0.0/Outcomes-a.txt). The dataset is publicly accessible under the **Open Data Commons Attribution License v1.0 (ODC-BY)**, as stated on the dataset page. Data use requires attribution. This dataset license does not establish a license for project code.

Raw data are stored locally under `data/raw/`, which is excluded from version control except for its directory placeholder. Raw data should not be committed.

### Citations

The provider requests the Challenge citation:

Silva I, Moody G, Scott DJ, Celi LA, Mark RG. Predicting in-hospital mortality of patients in ICU: The PhysioNet/Computing in Cardiology Challenge 2012. *Computing in Cardiology*. 2012;39:245-248. [Article](https://pmc.ncbi.nlm.nih.gov/articles/PMC3965265/).

The dataset page also requests the PhysioNet platform citation:

Pollard T, et al. PhysioNet as a global platform for biomedical research. *Nature Health*. 2026;1:792-795. [DOI](https://doi.org/10.1038/s44360-026-00096-z).

## Project structure

| Path | Purpose |
| --- | --- |
| `707-proposal.md` | Research question, cohort definitions, and planned analysis |
| `notebooks/01_data_exploration.ipynb` | Data loading, identifier checks, outcome summaries, and exploratory plotting code |
| `src/download_data.py` | Standalone download and extraction script |
| `data/raw/` | Local source archives, outcomes, and extracted patient files |
| `figures/` | Reserved for exported figures; currently contains a placeholder |
| `reports/` | Reserved for project reports; currently contains a placeholder |
| `pixi.toml` | Environment definition and dependencies |
| `pixi.lock` | Locked dependency resolution |
| `.gitignore` | Exclusions for raw data, environments, and temporary files |

Data exploration and subsequent modeling will remain in notebooks. The download script performs no analysis.

## Pixi environment setup

The existing Pixi manifest targets **Windows (`win-64`)** and Python 3.12. Dependencies include pandas, NumPy, SciPy, scikit-learn, Matplotlib, seaborn, JupyterLab, and ipykernel. Reproduction on another operating system would require an appropriate environment configuration.

From a PowerShell terminal in the project root, restore the locked environment:

```powershell
pixi install --locked
```

The command requires Pixi to be installed and available on the system path. Dependency installation may require internet access. Dependency changes should be accompanied by updates to both `pixi.toml` and `pixi.lock`.

## Reproducibility instructions

After restoring the environment, run the standalone downloader and launch JupyterLab from the project root:

```powershell
pixi run python src/download_data.py
pixi run jupyter lab
```

The downloader uses the Python standard library and retrieves only the two source files listed above. Existing downloads are reused. Archive destinations are checked before extraction into `data/raw/set-a/`; the current archive contains 4,000 patient files. Internet access is required when either source download is absent. The notebook also retains its original download logic.

Open `notebooks/01_data_exploration.ipynb`, select the project environment as the kernel, and execute all cells in order. The notebook locates the project root from either the project directory or `notebooks/`. Tables and plots are displayed within the notebook; the current code does not export figures automatically.

In VS Code, the Python and Jupyter extensions provide notebook execution. Select **Select Kernel > Python Environments** and choose `.pixi/envs/default/python.exe`, using **Enter interpreter path** if necessary, then select **Run All**.

### Verified local fallback

Pixi is installed in the inspected environment, but environment installation and `pixi run` currently fail because Pixi cannot determine the home directory. The command syntax was checked; successful Pixi execution has not been verified in this session. The existing environment interpreter and JupyterLab entry point were verified directly (Python 3.12.16 and JupyterLab 4.6.5). If the same Pixi error occurs and the environment already exists, the following PowerShell commands use it directly:

```powershell
.\.pixi\envs\default\python.exe src/download_data.py
.\.pixi\envs\default\python.exe -m jupyterlab
```

The downloader was previously executed successfully against existing local downloads and extracted 4,000 patient files. Fresh network downloading and a complete notebook rerun were not verified during this documentation update.

## Academic attribution and AI assistance

AI tools, including ChatGPT and Codex, were used to assist with environment configuration, debugging, and troubleshooting technical issues. The project proposal, including the research question, study design, and planned analytical methods, was written independently by the author.



