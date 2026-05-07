# Project Findings

## Overall point

This project is trying to understand roadwork at the street level in NYC by combining resurfacing activity, street reference data, seasonal weather summaries, plow coverage, and traffic volume.

The main task in the cleaned repo is: predict whether a street gets roadwork in a target summer season.

## Current data snapshot

- `data/derived/dot_to_cscl.csv` has `100,804` mapped DOT rows.
- `data/derived/street_weather.csv` has `119,990` rows across `11,999` streets.
- `data/derived/street_weather_daily.csv` has `599,950` rows across about `12,000` streets.
- `data/derived/resurfacing_agg_full.csv` has `20,671` street-season rows across `6,985` streets.
- `data/derived/traffic_agg.csv` covers `818` streets.
- `data/derived/plow_df.csv` has `69,078` rows across about `11,399` streets.
- `data/derived/street_weather_lagged_model.csv` has `276,000` rows spanning `2003` to `2025`.

## Modeling result

Using `data/derived/street_weather_lagged_model.csv` as the model table, a simple random-forest baseline produced:

- ROC-AUC: `0.5698`
- accuracy: `0.7607`
- positive-class precision: `0.1114`
- positive-class recall: `0.3476`

The table is imbalanced, with about `7.0%` positive roadwork cases.

The main pattern is that `roadwork_factor_summer_lag1` and `roadwork_factor_summer_lag2` matter most. Weather variables add some signal, but much less.

## Structural notes

- There was one main project spread across several overlapping notebooks.
- Some weather and normalization logic was duplicated.
- The main cleanup step was to separate the active workflow from the archived scratch notebooks.
- `GITHUB_NEWER` added a complete precomputed `plow_coverage` set and a cleaned decision-tree dataset, both now merged into the main workspace.

## Remaining blockers

- `data/raw/roadwork/dot_inhouse_resurfacing.csv` is present now, but it is still a manual input with no downloader code.
- The full raw plow file set under `data/raw/plow/` is still not present.
- Those raw plow files were not present in `GITHUB_NEWER` either.

So the project is organized and runnable from the cleaned snapshot, but not fully reproducible from raw plow inputs here.

## Provenance note

From the code, the plow raw chunks were meant to come from:

- `https://data.cityofnewyork.us/resource/rmhc-afj9.csv`

There is still no downloader code for `dot_inhouse_resurfacing.csv`, so that roadwork source still looks like a manual internal export.

## Recommended next move

If continuing from here, the next practical step is either to restore the full raw plow chunk set for a full rebuild, or to pull the model-table construction logic out of the archived legacy notebook into its own cleaned notebook.
