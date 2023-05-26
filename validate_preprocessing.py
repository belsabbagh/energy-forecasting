from src import dataset_handler

for country, df in dataset_handler.country_iter(directory="preprocessed"):
    print(f"Validating {country}... ", end="")
    if df.isnull().values.any():
        print("ERROR: NaN values found.")
        print(df[df.isnull().any(axis=1)])
        exit(1)
    print("Done.")
print("Validation complete. No errors found.")
