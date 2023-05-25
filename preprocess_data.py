import os
import pandas as pd
from src import dataset_handler


OUTPUT_DIRECTORY = "data/preprocessed"


def preprocess(df: pd.DataFrame) -> pd.DataFrame:
    """This is where you'll do your preprocessing. You should return a dataframe with the same columns as the input dataframe."""
    pass


if __name__ == "__main__":
    for country, df in dataset_handler.country_iter():
        df = preprocess(df)
        df.to_csv(os.path.join(OUTPUT_DIRECTORY, f"{country}.csv"))
