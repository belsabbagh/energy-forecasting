import os
import pandas as pd
from src import dataset_handler
import src.dataset_handler as dh

OUTPUT_DIRECTORY = "data/preprocessed"


def fill_country(df, dictionary):
    parents = [dh.get_country_data(parent) for parent in dictionary["parents"]]
    function = dictionary["function"]
    return function(df, parents)


def preprocess(df: pd.DataFrame) -> pd.DataFrame:
    def quad_btu_to_twh(quad_btu: float) -> float:
        return quad_btu * 293.071

    return df  # df.apply(quad_btu_to_twh)


def add_parent(df: pd.DataFrame, parents=list[pd.DataFrame]) -> pd.DataFrame:
    return df.combine_first(parents[0])


def ussr(df: pd.DataFrame, parents=list[pd.DataFrame]) -> pd.DataFrame:
    ratios = {
        "Russia": 0.75,
        "Ukraine": 0.1,
        "Kazakhstan": 0.05,
        "Uzbekistan": 0.05,
        "Turkmenistan": 0.025,
        "Belarus": 0.025,
        "Azerbaijan": 0.025,
        "Lithuania": 0.025,
        "Latvia": 0.025,
        "Estonia": 0.025,
        "Georgia": 0.025,
        "Armenia": 0.025,
        "Moldova": 0.025,
        "Kyrgyzstan": 0.025,
        "Tajikistan": 0.025,
    }
    return df.combine_first(parents[0] * ratios[df.name])


def double_parents(df: pd.DataFrame, parents=list[pd.DataFrame]) -> pd.DataFrame:
    return df.combine_first(add_parent(parents[1], [parents[0]]))


def triple_parents(df: pd.DataFrame, parents=list[pd.DataFrame]) -> pd.DataFrame:
    return df.combine_first(double_parents(parents[2], [parents[1], parents[0]]))


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
    "Armenia": {"function": ussr, "parents": ["Former U.S.S.R."]},
    "Aruba": {"function": add_parent, "parents": ["Netherlands"]},
    "Azerbaijan": {"function": ussr, "parents": ["Former U.S.S.R."]},
    "Belarus": {"function": ussr, "parents": ["Former U.S.S.R."]},
    "Bosnia and Herzegovina": {
        "function": add_parent,
        "parents": ["Former Yugoslavia"],
    },
    "Croatia": {"function": add_parent, "parents": ["Former Yugoslavia"]},
    "Czechia": {"function": add_parent, "parents": ["Former Czechoslovakia"]},
    "Eritrea": {"function": add_parent, "parents": ["Ethiopia"]},
    "Estonia": {"function": ussr, "parents": ["Former U.S.S.R."]},
    "Georgia": {"function": ussr, "parents": ["Former U.S.S.R."]},
    "Germany": {
        "function": Germany_parents,
        "parents": ["Germany, East", "Germany, West"],
    },
    "Kazakhstan": {"function": ussr, "parents": ["Former U.S.S.R."]},
    "Kosovo": {
        "function": triple_parents,
        "parents": ["Former Yugoslavia", "Former Serbia and Montenegro", "Serbia"],
    },
    "Kyrgyzstan": {"function": ussr, "parents": ["Former U.S.S.R."]},
    "Latvia": {"function": add_parent, "parents": ["Former U.S.S.R."]},
    "Lithuania": {"function": ussr, "parents": ["Former U.S.S.R."]},
    "Moldova": {"function": ussr, "parents": ["Former U.S.S.R."]},
    "Montenegro": {
        "function": double_parents,
        "parents": ["Former Yugoslavia", "Former Serbia and Montenegro"],
    },
    "Namibia": {"function": add_parent, "parents": ["South Africa"]},
    "North Macedonia": {"function": add_parent, "parents": ["Former Yugoslavia"]},
    "Northern Mariana Islands": {
        "function": add_parent,
        "parents": ["U.S. Pacific Islands"],
    },
    "Palestinian Territories": {"function": Palestine_parents, "parents": []},
    "Russia": {"function": ussr, "parents": ["Former U.S.S.R."]},
    "Serbia": {
        "function": double_parents,
        "parents": ["Former Yugoslavia", "Former Serbia and Montenegro"],
    },
    "Slovakia": {"function": add_parent, "parents": ["Former Czechoslovakia"]},
    "Slovenia": {"function": add_parent, "parents": ["Former Yugoslavia"]},
    "South Sudan": {"function": add_parent, "parents": ["Sudan"]},
    "Tajikistan": {"function": ussr, "parents": ["Former U.S.S.R."]},
    "Timor-Leste": {"function": add_parent, "parents": ["Indonesia"]},
    "Turkmenistan": {"function": ussr, "parents": ["Former U.S.S.R."]},
    "Ukraine": {"function": ussr, "parents": ["Former U.S.S.R."]},
    "Uzbekistan": {"function": ussr, "parents": ["Former U.S.S.R."]},
}

former_countries = dh.get_former_countries()
if __name__ == "__main__":
    for country, df in dataset_handler.country_iter():
        df.name = country
        if country in dictionary.keys():
            df = fill_country(df, dictionary[country])
        df = preprocess(df)
        if country not in former_countries:
            df.to_csv(os.path.join(OUTPUT_DIRECTORY, f"{country}.csv"))
