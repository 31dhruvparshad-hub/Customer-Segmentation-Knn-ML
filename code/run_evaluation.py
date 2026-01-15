import pandas as pd
from src.evaluate import evaluate_clusters

DATA_PATH = "data/processed/processed_data.csv"

def main():
    df = pd.read_csv(DATA_PATH)

    X = df.drop(columns=["cluster"], errors="ignore")
    labels = df["cluster"] if "cluster" in df.columns else None

    if labels is None:
        print("Run clustering first.")
        return

    score = evaluate_clusters(X, labels)
    print(f"Silhouette Score: {score:.2f}")

if __name__ == "__main__":
    main()

