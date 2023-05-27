from src import dataset_handler


if __name__ == "__main__":
    for country, df in dataset_handler.country_iter(directory="preprocessed"):
        print(f"Analyzing {country}... ", end="")
        df.corr(numeric_only=True).to_csv(f"out/analysis/correlation/{country}.csv")
        print("Done.")