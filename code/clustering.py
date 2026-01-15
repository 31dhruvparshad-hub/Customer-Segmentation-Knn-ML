import pandas as pd
from src.clustering import run_kmeans

DATA_PATH = "data/processed/processed_data.csv"

def main():
    df = pd.read_csv(DATA_PATH)

    model, labels = run_kmeans(df, n_clusters=5)
    df["cluster"] = labels

    print(df.head())

if __name__ == "__main__":
    main()
