# ==========================
# LOAD DATA MODULE
# ==========================

# Import pandas.
# Pandas is used for reading CSV files and working with tables.
import pandas as pd


# Create a function named load_data.
# A function is a reusable block of code.
# Instead of writing pd.read_csv() many times,
# we write it once and reuse it everywhere.
def load_data(file_path):

    # Read the CSV file.
    # file_path will be something like:
    # "../data/titanic.csv"
    df = pd.read_csv(file_path)

    # Return the DataFrame to whoever called this function.
    return df