from src.preprocess import load_and_preprocess_data

RAW_PATH = "data/raw/customer_shopping_data.csv"
PROCESSED_PATH = "data/processed/processed_data.csv"

def main():
    df = load_and_preprocess_data(RAW_PATH)
    df.to_csv(PROCESSED_PATH, index=False)
    print("Processed data saved to data/processed/processed_data.csv")

if __name__ == "__main__":
    main()
