import pandas as pd


def clean_data(df):
    df = df.copy()

    # Fill missing values
    df["Age"] = df["Age"].fillna(df["Age"].median())
    df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

    # Drop column with too many missing values
    df.drop(columns=["Cabin"], inplace=True)

    # Encode categorical columns
    df["Sex"] = df["Sex"].map({"female": 0, "male": 1})
    df = pd.get_dummies(df, columns=["Embarked"], drop_first=True)

    # Drop irrelevant columns
    df.drop(columns=["Name", "Ticket", "PassengerId"], inplace=True)

    return df
