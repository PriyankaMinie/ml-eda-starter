import pandas as pd

df_train = pd.read_csv("C:/Users/hp/Documents/ML-EDA-STARTER/data/train.csv")

print("Before filling:")
print(df_train["Age"].head(10))  # Show first 10 values for a quick view
print("Missing values:", df_train["Age"].isnull().sum())

df_train["Age"] = df_train["Age"].fillna(df_train["Age"].median())

print("\nAfter filling:")
print(df_train["Age"].head(10))
print("Missing values:", df_train["Age"].isnull().sum())

print("\nBefore filling:")
print(df_train["Embarked"].value_counts())  # Show first 10 values for a quick view
print("Missing values:", df_train["Embarked"].isnull().sum())

df_train["Embarked"] = df_train["Embarked"].fillna(df_train["Embarked"].mode()[0])

print("\nAfter filling:")
print(df_train["Embarked"].value_counts())  # Show first 10 values for a quick view
print("Missing values:", df_train["Embarked"].isnull().sum())

print("Before dropping Cabin:")
print(df_train[["Cabin"]].head(10))
print("Cabin" in df_train.columns)  # Should print True
print(df_train.head(1))  # To confirm Cabin is present
print("Missing values in Cabin:", df_train["Cabin"].isnull().sum())

df_train.drop(columns=["Cabin"], inplace=True)

print("\nAfter dropping Cabin:")
print("Cabin" in df_train.columns)  # Should print False
print(df_train.head(1))  # To confirm Cabin is gone

print("Before encoding 'Sex':")
print(df_train["Sex"].value_counts())
print(df_train["Sex"].head(10))

df_train["Sex"] = df_train["Sex"].map({"female": 0, "male": 1})

print("\nAfter encoding 'Sex':")
print(df_train["Sex"].value_counts())
print(df_train["Sex"].head(10))

print("\nBefore one-hot encoding 'Embarked':")
print(df_train[["Embarked"]].head())

df_train = pd.get_dummies(df_train, columns=["Embarked"], drop_first=True)

print("\nAfter one-hot encoding 'Embarked':")
print(df_train.head())

print("\nBefore dropping irrelevant columns:")
print(df_train.columns)

df_train.drop(columns=["Name", "Ticket", "PassengerId"], inplace=True)

print("\nAfter dropping irrelevant columns:")
print(df_train.columns)
