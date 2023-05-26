from matplotlib import pyplot as plt
import pandas as pd

from statsmodels.tsa.seasonal import seasonal_decompose
from src import dataset_handler


if __name__ == "__main__":
    for country, df in dataset_handler.country_iter():
        print(f"Analyzing {country}... ", end="")
        df.corr(numeric_only=True).to_csv(f"out/analysis/correlation/{country}.csv")
