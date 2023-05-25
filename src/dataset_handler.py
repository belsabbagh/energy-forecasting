from os import path
import os

import pandas as pd

DATASET_PATH = path.join("data", "generated")


def get_country_data(country: str) -> pd.DataFrame:
    """It should return a dataframe with the data for the given country."""
    raise NotImplementedError("get_country_data not implemented. Please implement it in dataset_handler.py")



def country_iter() -> tuple [str, pd.DataFrame]:
    """It should return a generator that yields the name and dataset of each country in the dataset."""
    raise NotImplementedError("country_iter not implemented. Please implement it in dataset_handler.py")
