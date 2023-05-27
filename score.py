import pandas as pd


# df = pd.read_csv("out/test_results/arima_eval.csv")

# df = pd.read_csv("out/test_results/rnn_eval.csv")

df = pd.read_csv("out/test_results/lstm_eval.csv")

# df = pd.read_csv("out/test_results/gru_eval.csv")

df = df.drop(columns=["Unnamed: 0"])

print(df.groupby("Resource").mean())
