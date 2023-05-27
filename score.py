import pandas as pd


# df = pd.read_csv("out/test_results/arima_eval.csv")

# df = pd.read_csv("out/test_results/rnn_eval.csv")

# df = pd.read_csv("out/test_results/lstm_eval.csv")

# df = pd.read_csv("out/test_results/gru_eval.csv")

df = pd.read_csv("out/test_results/wa_eval.csv")

df = df.drop(columns=["Unnamed: 0"])

res = df.groupby("Resource").mean()
print (res)
res.to_csv("out/test_results/wa_eval_mean.csv")