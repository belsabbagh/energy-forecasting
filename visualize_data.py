from os import path
from matplotlib import pyplot as plt
from src import dataset_handler as dh
from statsmodels.tsa.seasonal import seasonal_decompose

CHARTS_PATH = path.join("out", "charts")


for country, df in dh.country_iter(directory="preprocessed"):
    df.dropna(inplace=True)
    for r in df.columns:
        title = f"{country}_{r}"
        plot = seasonal_decompose(df[[r]], period=5, model="additive").plot()
        plot.suptitle(title)
        plot.savefig(path.join(CHARTS_PATH, "patterns", f"{title}.png"))
        plt.close()
    plot = df.plot(ylim=(0, None))
    plot.set_ylabel("Energy (TWh)")
    plot.set_xlabel("Year")
    plot.legend(loc="upper right", fontsize=7)
    plt.savefig(path.join(CHARTS_PATH, "overviews", f"{country}.png"), dpi=300)
    plt.close()
    print(f"Visualized {country}")
