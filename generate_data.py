import os
import pandas as pd


from os import path


def file_iter():
    for folder in os.listdir("data"):
        if path.isfile(path.join("data", folder)) or folder.startswith("generated"):
            continue
        for filename in os.listdir(path.join("data", folder)):
            if not filename.endswith(".csv"):
                continue
            df = pd.read_csv(path.join("data", folder, filename), index_col="Country")
            df.index = df.index.str.strip()
            df.drop(columns=["Continent"], inplace=True)
            yield filename, df


def get_attr_from_filename(filename):
    stat, src = filename.split("_")
    return stat, src.split(".")[0]


def collect_country_data(country) -> pd.DataFrame:
    country_data = {}
    for name, df in file_iter():
        if country not in df.index:
            continue
        stat, src = get_attr_from_filename(name)
        country_data[f"{stat}_{src}"] = df.loc[country].iloc[:-1]
    res = pd.DataFrame(country_data)
    res.index.name = "Year"
    return res

def get_countries():
    countries = set()
    for _, df in file_iter():
        countries.update(df.index)
    return countries

if __name__ == "__main__":
    for country in get_countries():
        df = collect_country_data(country)
        df.to_csv(path.join("data", "generated", f"{country}.csv"))