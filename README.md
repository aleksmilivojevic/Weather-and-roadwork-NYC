<<<<<<< HEAD
# NYC Street Weather / Roadwork Project

## Project point

This project builds street-level NYC features to see whether weather, plow activity, traffic, and prior roadwork help explain or predict later resurfacing / roadwork activity.

The repo is notebook-first. The main workflow is now separated from the older scratch work.

## Public data sources visible from the code

- NYC Open Data plow feed:
  `https://data.cityofnewyork.us/resource/rmhc-afj9.csv`
- NYC traffic counts:
  reflected in the bundled `traffic_1.csv` and `traffic_2.csv`
- Open-Meteo historical weather:
  reflected in the bundled hourly and daily weather files

`dot_inhouse_resurfacing.csv` is in the workspace, but there is no downloader code for it in the repo. It looks like a manual DOT in-house export.

## Cleaned layout

- `01_dot_to_cscl_mapping.ipynb`
  Maps DOT street names to CSCL street names.
- `02_build_resurfacing_features.ipynb`
  Builds the resurfacing street-season table.
- `03_build_street_weather_features.ipynb`
  Builds the street weather tables.
- `04_build_traffic_features.ipynb`
  Builds the traffic table.
- `05_process_plow_features.ipynb`
  Builds or inspects plow-derived features.
- `06_model_roadwork_weather.ipynb`
  Runs the baseline model.
- `07_project_findings.ipynb`
  Checks the current project state.

- `data/reference/`
  Reference data such as `CSCL.csv` and LION/SND files.
- `data/raw/`
  Raw inputs.
- `data/derived/`
  Derived tables and outputs.
- `reports/`
  Markdown summaries.
- `archive/`
  Older notebooks not used in the main workflow.

## Main workflow

1. Keep `data/raw/roadwork/dot_inhouse_resurfacing.csv` in place.
2. Run `01_dot_to_cscl_mapping.ipynb`.
3. Run `02_build_resurfacing_features.ipynb`.
4. Run `03_build_street_weather_features.ipynb`.
5. Run `04_build_traffic_features.ipynb`.
6. Use the bundled plow-derived outputs as-is, or run `05_process_plow_features.ipynb` if you have the full raw `data/raw/plow/plow_*.csv` set and want to rebuild them.
7. Run `06_model_roadwork_weather.ipynb`.
8. Use `07_project_findings.ipynb` and `reports/project_findings.md` for the current summary.

## What was merged from `GITHUB_NEWER`

- `plow_coverage_0.csv` through `plow_coverage_39.csv` were merged into `data/derived/plow_coverage/`.
- `decisiontree_cleaned_data.csv` was merged into `data/derived/decisiontree_cleaned_data.csv`.
- The decision-tree notebook was kept in `archive/decisiontree_regression_experiment.ipynb`.

This helped fill in derived outputs, but it did not recover the full raw plow chunk set.

## Current limits

- The roadwork raw export is present, but it is still a manual input with no downloader code in the repo.
- The full raw plow chunk set `data/raw/plow/plow_*.csv` is still not present.
- Those raw plow files were not in `GITHUB_NEWER` either.

So the cleaned workflow runs from the current snapshot, but full raw plow regeneration is still not set up here.

## What you can run now

- You can rerun the mapping, resurfacing, weather, traffic, modeling, and findings notebooks from this workspace.
- You can use the bundled `plow_coverage` outputs and `plow_df.csv` without rebuilding them.
- You only need raw plow chunk files if you want to rebuild the plow part from scratch.

## GitHub notes

- The repo is set up to publish the cleaned notebooks, helper scripts, docs, reference data, and derived CSV outputs.
- `.gitignore` excludes the manual roadwork raw export, partial raw plow chunk files, cache files, and the local DuckDB scratch file.
- For a public repo, keep those ignores in place.
- For a private full-data repo, you can add the raw files intentionally.

## Current snapshot findings

- `dot_to_cscl.csv`: 100,804 rows
- `street_weather.csv`: 119,990 rows
- `street_weather_daily.csv`: 599,950 rows
- `resurfacing_agg_full.csv`: 20,671 rows
- `traffic_agg.csv`: 818 streets
- `plow_df.csv`: 69,078 rows
- `street_weather_lagged_model.csv`: 276,000 rows
- positive class rate in the lagged model table: about `7.0%`

A simple random-forest baseline on the lagged model table reached about:

- ROC-AUC: `0.5698`
- positive-class precision: `0.1114`
- positive-class recall: `0.3476`

The strongest predictors were prior-summer roadwork features. Weather variables mattered less.
=======
# Weather-and-roadwork-NYC
NYC street-level roadwork analysis using resurfacing, weather, plow, and traffic data.
>>>>>>> fc9d6d6298aab6127571b4af674d235e5b2d2faa
