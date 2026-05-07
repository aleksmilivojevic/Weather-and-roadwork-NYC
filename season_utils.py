import pandas as pd


def split_season_year(df: pd.DataFrame, column: str = "normalized_street_name_season") -> pd.DataFrame:
    parts = df[column].str.extract(r"^(.*)_(winter|summer|roadwork)_(\d{4})$")
    parts.columns = ["normalized_street_name", "season", "year"]

    out = df.copy()
    out[["normalized_street_name", "season", "year"]] = parts
    out["season"] = out["season"].str.lower()
    out["year"] = pd.to_numeric(out["year"], errors="coerce").astype("Int64")
    return out
