import os
import pandas as pd
from src import dataset_handler
import src.dataset_handler as dh

OUTPUT_DIRECTORY = "data/preprocessed"


def fill_country(df, dictionary):
    parents = [
        dh.get_country_data(parent) for parent in dictionary["parents"]
    ]
    function = dictionary["function"]
    return function(df, parents)


def preprocess(df: pd.DataFrame) -> pd.DataFrame:
    def quad_btu_to_twh(quad_btu: float) -> float:
        return quad_btu * 293.071
    return df.apply(quad_btu_to_twh)


def add_parent(df: pd.DataFrame, parents=list[pd.DataFrame]) -> pd.DataFrame:
    df = df.combine_first(parents[0])
    return df


def double_parents(df: pd.DataFrame, parents=list[pd.DataFrame]) -> pd.DataFrame:
    return df.combine_first(add_parent(parents[1], [parents[0]]))


def Germany_parents(df: pd.DataFrame, parents=list[pd.DataFrame]) -> pd.DataFrame:
    return df.combine_first(sum(parents))


def Palestine_parents(df: pd.DataFrame, parents=list[pd.DataFrame]) -> pd.DataFrame:
    for column in df.columns:
        if column.startswith("Production"):
            df[column].fillna(0, inplace=True)
        if column.startswith("Consumption"):
            df[column].fillna(df[column].mean(), inplace=True)
    return df


dictionary = {
    "Armenia": {
        "function": add_parent,
        "parents": ["Former U.S.S.R."]
    },
    "Aruba": {
        "function": add_parent,
        "parents": ["Netherlands"]
    },
    "Azerbaijan": {
        "function": add_parent,
        "parents": ["Former U.S.S.R."]
    },
    "Belarus": {
        "function": add_parent,
        "parents": ["Former U.S.S.R."]
    },
    "Bosnia and Herzegovina": {
        "function": add_parent,
        "parents": ["Former Yugoslavia"]
    },
    "Croatia": {
        "function": add_parent,
        "parents": ["Former Yugoslavia"]
    },
    "Czechia": {
        "function": add_parent,
        "parents": ["Former Czechoslovakia"]
    },
    "Eritrea": {
        "function": add_parent,
        "parents": ["Ethiopia"]
    },
    "Estonia": {
        "function": add_parent,
        "parents": ["Former U.S.S.R."]
    },
    "Georgia": {
        "function": add_parent,
        "parents": ["Former U.S.S.R."]
    },
    "Germany": {
        "function": Germany_parents,
        "parents": ["Germany, East", "Germany, West"]
    },
    "Kazakhstan": {
        "function": add_parent,
        "parents": ["Former U.S.S.R."]
    },
    "Kosovo": {
        "function": add_parent,
        "parents": ["Serbia"]
    },
    "Kyrgyzstan": {
        "function": add_parent,
        "parents": ["Former U.S.S.R."]
    },
    "Latvia": {
        "function": add_parent,
        "parents": ["Former U.S.S.R."]
    },
    "Lithuania": {
        "function": add_parent,
        "parents": ["Former U.S.S.R."]
    },
    "Moldova": {
        "function": add_parent,
        "parents": ["Former U.S.S.R."]
    },
    "Montenegro": {
        "function": double_parents,
        "parents": ["Former Yugoslavia", "Former Serbia and Montenegro"]
    },
    "Namibia": {
        "function": add_parent,
        "parents": ["South Africa"]
    },
    "North Macedonia": {
        "function": add_parent,
        "parents": ["Former Yugoslavia"]
    },
    "Northern Mariana Islands": {
        "function": add_parent,
        "parents": ["U.S. Pacific Islands"]
    },
    "Palestinian Territories": {
        "function": Palestine_parents,
        "parents": []
    },
    "Russia": {
        "function": add_parent,
        "parents": ["Former U.S.S.R."]
    },
    "Serbia": {
        "function": double_parents,
        "parents": ["Former Yugoslavia", "Former Serbia and Montenegro"]
    },
    "Slovakia": {
        "function": add_parent,
        "parents": ["Former Czechoslovakia"]
    },
    "Slovenia": {
        "function": add_parent,
        "parents": ["Former Yugoslavia"]
    },
    "South Sudan": {
        "function": add_parent,
        "parents": ["Sudan"]
    },
    "Tajikistan": {
        "function": add_parent,
        "parents": ["Former U.S.S.R."]
    },
    "Timor-Leste": {
        "function": add_parent,
        "parents": ["Indonesia"]
    },
    "Turkmenistan": {
        "function": add_parent,
        "parents": ["Former U.S.S.R."]
    },
    "Ukraine": {
        "function": add_parent,
        "parents": ["Former U.S.S.R."]
    },
    "Uzbekistan": {
        "function": add_parent,
        "parents": ["Former U.S.S.R."]
    }
}

if __name__ == "__main__":
    for country, df in dataset_handler.country_iter():
        if country in dictionary.keys():
            df = fill_country(df, dictionary[country])
        df = preprocess(df)
        df.to_csv(os.path.join(OUTPUT_DIRECTORY, f"{country}.csv"))
