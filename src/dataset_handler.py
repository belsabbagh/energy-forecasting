from os import path, listdir

import pandas as pd

DATA_PATH = path.join("data")
DEFAULT_DIR = "generated"


def get_country_data(country: str, directory=DEFAULT_DIR) -> pd.DataFrame:
    csvpath = path.join(DATA_PATH, directory, f"{country}.csv")
    df = pd.read_csv(csvpath, index_col="Year")
    if df is None:
        return None
    df.index = df.index.astype(int)
    return df


def country_iter(directory=DEFAULT_DIR) -> tuple[str, pd.DataFrame]:
    for filename in listdir(path.join(DATA_PATH, directory)):
        if not filename.endswith(".csv"):
            continue
        country = filename.rsplit(".", 1)[0]
        yield country, get_country_data(country)
