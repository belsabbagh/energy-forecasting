from keras.models import Sequential
from keras.layers import Dense, GRU
import pandas as pd
from src import dataset_handler as dh
from src.tester import evaluate_model, evaluate_multi_feature_model

n_features = 1
n_steps = 5

model = Sequential()
model.add(GRU(50, activation="relu", input_shape=(n_steps, n_features)))
model.add(Dense(1))
model.compile(optimizer="adam", loss="mse")

if __name__ == "__main__":
    results = pd.DataFrame(
        {"Country": [], "Resource": [], "mse": [], "rmse": [], "mae": []}
    )
    for country, df in dh.country_iter(directory="preprocessed"):
        print(f"GRU: Evaluating {country}... ", end="")
        results_df = pd.DataFrame(evaluate_model(model, df))
        results_df["Resource"] = results_df.index
        results_df = results_df.reset_index(drop=True)
        results_df["Country"] = country
        results = pd.concat([results, results_df])
        print(f"Done.")
    results.to_csv(f"out/test_results/gru_eval.csv")
