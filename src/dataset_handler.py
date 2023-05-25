from os import path
import os

import pandas as pd

DATASET_PATH = path.join("data", "generated")


def get_country_data(country: str) -> pd.DataFrame:
    csvpath = path.join(DATASET_PATH, f"{country}.csv")
    df = pd.read_csv(csvpath, index_col="Year")
    if df is None:
        return None
    df.index = df.index.astype(int)
    return df


def country_iter() -> tuple[str, pd.DataFrame]:
    for filename in os.listdir(DATASET_PATH):
        if not filename.endswith(".csv"):
            continue
        country = filename.rsplit(".", 1)[0]
        yield country, get_country_data(country)
