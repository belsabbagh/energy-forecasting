import os
import pandas as pd


from os import path


def file_iter():
    for folder in os.listdir("data"):
        if folder not in ["Consumption_Data", "Production_Data"]:
            continue
        for filename in os.listdir(path.join("data", folder)):
            if not filename.endswith(".csv"):
                continue
            df = pd.read_csv(path.join("data", folder, filename), index_col="Country")
            df.drop(columns=["Continent"], inplace=True)
            yield filename, df


def get_attr_from_filename(filename):
    stat, src = filename.split("_")
    return stat, src.split(".")[0]


def collect_country_data(country: str) -> pd.DataFrame:
    def drop_if_exists(df, col):
        if col in df.columns:
            df.drop([col], axis=1, inplace=True)

    country_data = {}
    for name, df in file_iter():
        df.index = df.index.str.strip().str.replace("/", "-")
        if country not in df.index:
            continue
        stat, src = get_attr_from_filename(name)
        country_data[f"{stat}_{src}"] = df.loc[country].iloc[:-1]
    res = pd.DataFrame(country_data)
    res.index.name = "Year"
    drop_if_exists(res, "Consumption_Total")
    drop_if_exists(res, "Production_Total")
    return res


def get_countries():
    countries = set()
    for _, df in file_iter():
        countries.update(df.index.str.strip().str.replace("/", "-"))
    return countries


if __name__ == "__main__":
    for country in get_countries():
        df = collect_country_data(country)
        df.to_csv(path.join("data", "generated", f"{country}.csv"))
        active_range = list(df.dropna(inplace=False).index)
