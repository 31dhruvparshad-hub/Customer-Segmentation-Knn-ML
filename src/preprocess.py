import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_and_preprocess_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)

    # Select useful columns for customer behavior
    df = df[["age", "quantity", "price"]]

    # Drop missing values
    df = df.dropna()

    # Scale features (important for K-Means)
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df)

    df_scaled = pd.DataFrame(
        scaled_data,
        columns=df.columns
    )

    return df_scaled
