from src import dataset_handler


for country, df in dataset_handler.country_iter():
    df.corr(numeric_only=True).to_csv(f"out/analysis/correlation/{country}.csv")
