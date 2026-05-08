# Weather and Roadwork in NYC

This project looks at roadwork at the street level in New York City.

The main question is whether winter weather and related street conditions help explain or predict where resurfacing happens later. To get at that, we combine roadwork records with street reference data, weather summaries, plow coverage, and traffic data, then built a street-level modeling table.

## Overview

At a high level, this repo does three things:

1. takes roadwork data and maps it onto a consistent street reference
2. builds street-level feature tables from weather, plow, and traffic data
3. uses those features to study and predict later summer roadwork

The repo is notebook-based because most of the work here was exploratory and iterative, but the main workflow is now separated from older scratch work.

## Data used

The project combines a few different sources:

- DOT resurfacing / roadwork records
- CSCL, the Citywide Street Centerline file, used as the street reference table
- historical weather data
- plow coverage data
- traffic count data

In the notebooks:

- `DOT` means New York City Department of Transportation
- `CSCL` means Citywide Street Centerline

A key early step is mapping the street names in the DOT resurfacing data onto CSCL street names so everything can be joined consistently later.

## Notebooks

- `01_dot_to_cscl_mapping.ipynb`
  Maps DOT street names to CSCL street names.
- `02_build_resurfacing_features.ipynb`
  Cleans the resurfacing data and builds the street-season resurfacing table.
- `03_build_street_weather_features.ipynb`
  Assigns streets to weather stations and builds street-level weather tables.
- `04_build_traffic_features.ipynb`
  Cleans and aggregates the traffic data.
- `05_process_plow_features.ipynb`
  Processes plow data and builds plow-derived coverage features.
- `06_model_roadwork_weather.ipynb`
  Runs the baseline model and contains the actual model results.
- `07_project_findings.ipynb`
  Summarizes the current project state and data snapshot.

## Repository layout

- `data/reference/`
  Street reference files and related materials.
- `data/raw/`
  Raw inputs used by the notebooks.
- `data/derived/`
  Derived tables produced by the pipeline.
- `archive/`
  Older notebooks and scratch work that are not part of the main workflow.
- `reports/`
  Short written summaries.

## Main result

The main modeling table in this repo is `data/derived/street_weather_lagged_model.csv`.

Using that table, a simple random forest baseline gives:

- ROC-AUC: `0.5698`
- positive-class precision: `0.1114`
- positive-class recall: `0.3476`

These results are in `06_model_roadwork_weather.ipynb`.

The main pattern is that prior roadwork matters more than weather. Weather adds some signal, but the strongest predictors are the lagged roadwork features, especially whether a street had roadwork in recent summers.

So the current project is more convincing as a persistence-style roadwork prediction problem than as a strong weather-only explanation.

## How to run

The main workflow is:

1. run `01_dot_to_cscl_mapping.ipynb`
2. run `02_build_resurfacing_features.ipynb`
3. run `03_build_street_weather_features.ipynb`
4. run `04_build_traffic_features.ipynb`
5. use the bundled plow-derived outputs, or rerun `05_process_plow_features.ipynb` if you have the full raw plow files
6. run `06_model_roadwork_weather.ipynb` for the model results
7. look at `07_project_findings.ipynb` for the project summary and dataset snapshot

## Notes

- Some raw files are not included in the public-facing version of the repo.
- The roadwork raw file appears to be a manual DOT export rather than something downloaded directly by repository code.
- The raw plow chunk set is not fully included here, but the derived plow outputs used later in the project are present.

## Files worth starting with

If you are opening this repo for the first time, the best places to start are:

- `01_dot_to_cscl_mapping.ipynb`
- `03_build_street_weather_features.ipynb`
- `06_model_roadwork_weather.ipynb`
- `07_project_findings.ipynb`
