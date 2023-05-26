from os import path
from matplotlib import pyplot as plt
import pandas as pd
from src import dataset_handler
from statsmodels.tsa.seasonal import seasonal_decompose

CHARTS_PATH = path.join("out", "charts")


def plot_patterns(df: pd.DataFrame):
    for r in df.columns:
        plot = seasonal_decompose(df[[r]], period=2, model="additive").plot()
        plot.savefig(path.join(CHARTS_PATH, "patterns", f"{country}_{r}.png"))
        plt.close()
    return


for country, df in dataset_handler.country_iter():
    df.dropna(inplace=True)
    plot_patterns(df)
    plot = df.plot(ylim=(0, None))
    plot.set_ylabel("Energy (Quadrillion BTU)")
    plot.set_xlabel("Year")
    plot.legend(loc="upper right", fontsize=7)
    plt.savefig(path.join(CHARTS_PATH, "overviews", f"{country}.png"), dpi=300)
    plt.close()
    print(f"Visualized {country}")
