# Import the function used to split the dataset.
from sklearn.model_selection import train_test_split

# Import the Logistic Regression algorithm.
from sklearn.linear_model import LogisticRegression

# import evalvatoin metrics
from sklearn.metrics import confusion_matrix,accuracy_score,classification_report


# Split the dataset into training and testing sets.
def split_data(X, y):

    # Split the data.
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    # Return the split datasets.
    return X_train, X_test, y_train, y_test


# Train the machine learning model.
def train_model(X_train, y_train):

    # Create the model.
    model = LogisticRegression(max_iter=1000)

    # Train the model.
    model.fit(X_train, y_train)

    # Return the trained model.
    return model

# Make predictions using the trained model.
def predict_model(model, X_test):

    # Predict the target values.
    predictions = model.predict(X_test)

    # Return the predictions.
    return predictions


# Evaluate the model.
def evaluate_model(y_test, predictions):

    # Calculate the accuracy.
    accuracy = accuracy_score(y_test, predictions)

    # Create the confusion matrix.
    cm = confusion_matrix(y_test, predictions)

    # Create the classification report.
    report = classification_report(y_test, predictions)

    # Return all evaluation results.
    return accuracy, cm, report

