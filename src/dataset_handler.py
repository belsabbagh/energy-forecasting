from os import path, listdir

import pandas as pd

DATA_PATH = path.join("data")
DEFAULT_DIR = "generated"


def get_country_data(country: str, directory=DEFAULT_DIR) -> pd.DataFrame:
    csvpath = path.join(DATA_PATH, directory, f"{country}.csv")
    df = pd.read_csv(csvpath, index_col="Year", parse_dates=[0])
    if df is None:
        return None
    return df


def country_iter(directory=DEFAULT_DIR) -> tuple[str, pd.DataFrame]:
    for filename in listdir(path.join(DATA_PATH, directory)):
        if not filename.endswith(".csv"):
            continue
        country = filename.rsplit(".", 1)[0]
        yield country, get_country_data(country, directory)


def get_former_countries():
    return [country for country, df in country_iter() if df.iloc[-1].isna().any()]
