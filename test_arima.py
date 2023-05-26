import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMA

from src.dataset_handler import get_country_data

# Load the dataset
data = get_country_data("Egypt")

results = {}
for column in data.columns:
    series = data[column]
    train_data, test_data = series.iloc[:20], series.iloc[20:]
    model = ARIMA(
        train_data, order=(1, 0, 0)
    )  # Replace p, d, q with appropriate values

    # Fit the model to the training data
    model_fit = model.fit()

    # Make predictions on the test data
    predictions = model_fit.predict(
        start=len(train_data), end=len(train_data) + len(test_data) + 2
    )

    # Evaluate the model
    mse = np.mean((predictions - test_data) ** 2)
    rmse = np.sqrt(mse)
    mae = np.mean(np.abs(predictions - test_data))
    results[column] = {
        # "predictions": predictions,
        "mse": mse,
        "rmse": rmse,
        "mae": mae,
    }
print(results)
