from os import path
import os

import pandas as pd

DATA_PATH = path.join("data")


def get_country_data(country: str, directory="generated") -> pd.DataFrame:
    csvpath = path.join("data", directory, f"{country}.csv")
    df = pd.read_csv(csvpath, index_col="Year")
    if df is None:
        return None
    df.index = df.index.astype(int)
    return df


def country_iter(directory="generated") -> tuple[str, pd.DataFrame]:
    for filename in os.listdir(path.join(DATA_PATH, directory)):
        if not filename.endswith(".csv"):
            continue
        country = filename.rsplit(".", 1)[0]
        yield country, get_country_data(country)
