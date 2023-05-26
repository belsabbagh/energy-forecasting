import warnings
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error

from src.dataset_handler import country_iter

warnings.filterwarnings("ignore")

results = pd.DataFrame({"Country": [], "Resource": [], "mse": [], "rmse": []})
for country, df in country_iter(directory="preprocessed"):
    print(f"ARIMA: Evaluating {country}... ", end="")
    for column in df.columns:
        series = df[column]
        train_data, test_data = series.iloc[:30], series.iloc[30:]
        model = ARIMA(
            train_data, order=(1, 1, 1), freq="AS-JAN"
        )  # Replace p, d, q with appropriate values

        # Fit the model to the training data
        model_fit = model.fit()

        # Make predictions on the test data
        predictions = model_fit.predict(
            start=len(train_data), end=len(train_data) + len(test_data) - 1
        )

        res = pd.DataFrame(
            {
                "Country": [country],
                "Resource": [column],
                "mse": [mean_squared_error(test_data, predictions)],
                "rmse": [mean_squared_error(test_data, predictions, squared=False)],
            }
        )
        results = pd.concat([results, res])
    print(f"Done.")
results.to_csv(f"out/test_results/arima_eval.csv")
