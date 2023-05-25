from os import path
from matplotlib import pyplot as plt
from src import dataset_handler

CHARTS_PATH = path.join("out", "charts")

for country, df in dataset_handler.country_iter():
    df.dropna()
    plot = df.plot(ylim=(0,None))
    plot.set_ylabel("Energy (Quadrillion BTU)")
    plot.set_xlabel("Year")
    plot.legend(loc="upper right", fontsize=7)
    plt.savefig(path.join(CHARTS_PATH, f"{country}.png"), dpi=300)
    plt.close()
    print(f"Visualized {country}")
