from os import path
from matplotlib import pyplot as plt
from src import dataset_handler

CHARTS_PATH = path.join("out", "charts")

for country, df in dataset_handler.country_iter():
    df.dropna()
    df.plot()
    plt.savefig(path.join(CHARTS_PATH, f"{country}.png"), dpi=300)
    plt.close()
    print(f"Visualized {country}")
