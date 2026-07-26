# ==========================
# PREPROCESSING MODULE
# ==========================

# Import pandas.
# We need pandas because our functions will work with DataFrames.
import pandas as pd


# Function 1
# --------------------------
# Display basic information about the dataset.
def dataset_info(df):

    # Print a title so the output is easy to read.
    print("=" * 50)
    print("DATASET INFORMATION")
    print("=" * 50)

    # Print information about every column.
    # It shows:
    # - Column names
    # - Number of non-missing values
    # - Data types
    df.info()

    # Print an empty line for better formatting.
    print()


# Function 2
# --------------------------
# Display the number of missing values.
def missing_values(df):

    print("=" * 50)
    print("MISSING VALUES")
    print("=" * 50)

    # Count missing values in every column.
    print(df.isnull().sum())

    print()


# Function 3
# --------------------------
# Display statistical information.
def summary_statistics(df):

    print("=" * 50)
    print("SUMMARY STATISTICS")
    print("=" * 50)

    # Show statistics for numerical columns.
    print(df.describe())

    print()


# Function 4
# --------------------------
# Display the first rows of the dataset.
def preview_data(df):

    print("=" * 50)
    print("FIRST FIVE ROWS")
    print("=" * 50)

    print(df.head())

    print()

# ==========================
# DATA CLEANING FUNCTIONS
# ==========================


# Fill missing values in the Age column.
def fill_age(df):

    # Calculate the average age.
    average_age = df["age"].mean()

    # Replace missing values.
    df["age"] = df["age"].fillna(average_age)

    # Return the updated DataFrame.
    return df


# Fill missing values in the Embarked column.
def fill_embarked(df):

    # Find the most common value.
    most_common = df["embarked"].mode()[0]

    # Replace missing values.
    df["embarked"] = df["embarked"].fillna(most_common)

    return df


# Fill missing values in embark_town.
def fill_embark_town(df):

    # Find the most common town.
    most_common = df["embark_town"].mode()[0]

    # Replace missing values.
    df["embark_town"] = df["embark_town"].fillna(most_common)

    return df


# Remove the deck column.
def drop_deck(df):

    # Drop the deck column.
    df = df.drop(columns=["deck"])

    return df


# Complete preprocessing function.
# This function performs all cleaning steps.
def preprocess_data(df):

    # Fill Age values.
    df = fill_age(df)

    # Fill Embarked values.
    df = fill_embarked(df)

    # Fill embark_town values.
    df = fill_embark_town(df)

    # Remove deck column.
    df = drop_deck(df)

    # Return cleaned dataset.
    return df

# ==========================
# FEATURE ENGINEERING
# ==========================


# Convert text columns into numbers.
def encode_features(df):

    # Convert "male" and "female" into numbers.
    df["sex"] = df["sex"].map({
        "male": 1,
        "female": 0
    })

    # Convert embarked values into numbers.
    df["embarked"] = df["embarked"].map({
        "S": 0,
        "C": 1,
        "Q": 2
    })

    # Return the updated DataFrame.
    return df


# Prepare data for machine learning.
def prepare_data(df):

    # Remove columns that won't be used for training.
    df = df.drop(
        columns=[
            "class",
            "who",
            "adult_male",
            "embark_town",
            "alive"
        ]
    )

    # Separate input features from the target.
    X = df.drop(columns=["survived"])

    # Target column.
    y = df["survived"]

    # Return both.
    return X, y