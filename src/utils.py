# Import joblib.
import joblib

# Import pandas.
import pandas as pd


# Save a trained machine learning model.
def save_model(model, file_path):

    # Save the model.
    joblib.dump(model, file_path)

    print(f"Model saved to: {file_path}")


# Load a trained machine learning model.
def load_model(file_path):

    # Load the model.
    model = joblib.load(file_path)

    return model


# Save a DataFrame as a CSV file.
def save_dataframe(df, file_path):

    # Save the DataFrame.
    df.to_csv(file_path, index=False)

    print(f"Data saved to: {file_path}")