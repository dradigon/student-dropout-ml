import pandas as pd
import joblib
from lightgbm import LGBMClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from src.preprocess import preprocess_features


def clean_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = (
        df.columns
        .str.strip()
        .str.replace(" ", "_")
        .str.replace("(", "", regex=False)
        .str.replace(")", "", regex=False)
        .str.replace("/", "_")
        .str.replace("'", "", regex=False)
    )
    return df


def main():
    # 1️⃣ Load dataset
    df = pd.read_csv("data/students.csv", sep=";")

    # 2️⃣ Clean column names
    df = clean_columns(df)

    # 3️⃣ Split features and target
    X = df.drop(columns=["Target"])
    y_raw = df["Target"]

    # 4️⃣ Encode target labels
    label_encoder = LabelEncoder()
    y = label_encoder.fit_transform(y_raw)

    # 5️⃣ Preprocess features
    X = preprocess_features(X)

    # 6️⃣ Train-validation split
    X_train, X_val, y_train, y_val = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    # 7️⃣ Train LightGBM model
    model = LGBMClassifier(
        objective="multiclass",
        num_class=3,
        random_state=42,
        n_estimators=300,
        learning_rate=0.05
    )

    model.fit(X_train, y_train, categorical_feature="auto")

    # 8️⃣ Save model and encoder
    joblib.dump(model, "model/lgbm_model.pkl")
    joblib.dump(label_encoder, "model/label_encoder.pkl")

    print("✅ Training complete. Model and encoder saved.")


if __name__ == "__main__":
    main()
