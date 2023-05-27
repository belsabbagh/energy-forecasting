import warnings
import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error

from src.dataset_handler import country_iter

warnings.filterwarnings("ignore")


def weightedmovingaverage(Data, period):
    weights = np.arange(1, period + 1)
    weights = weights / weights.sum()
    a = np.convolve(Data, weights, mode="full")[: len(Data)]
    a[:period] = a[period]
    return a


results = pd.DataFrame({"Country": [], "Resource": [], "mse": [], "rmse": []})
for country, df in country_iter(directory="preprocessed"):
    print(f"Weighted Average: Evaluating {country}... ", end="")
    for column in df.columns:
        series = df[column]
        train_data, test_data = series.iloc[:30], series.iloc[30:]
        predictions = weightedmovingaverage(series, 5)
        res = pd.DataFrame(
            {
                "Country": [country],
                "Resource": [column],
                "mse": [mean_squared_error(series, predictions)],
                "rmse": [mean_squared_error(series, predictions, squared=False)],
                "mae": [mean_absolute_error(series, predictions)],
            }
        )
        results = pd.concat([results, res])
    print(f"Done.")
results.to_csv(f"out/test_results/wa_eval.csv")
