# Import Matplotlib.
import matplotlib.pyplot as plt

# Import Seaborn.
import seaborn as sns


# Plot the survival distribution.
def plot_survival(df):

    # Create a new figure.
    plt.figure(figsize=(6, 4))

    # Create the count plot.
    sns.countplot(data=df, x="survived")

    # Add the title.
    plt.title("Survival Distribution")

    # Add axis labels.
    plt.xlabel("Survived")
    plt.ylabel("Number of Passengers")

    # Display the plot.
    plt.show()


# Plot the age distribution.
def plot_age(df):

    # Create a new figure.
    plt.figure(figsize=(8, 5))

    # Create the histogram.
    sns.histplot(df["age"], bins=30, kde=True)

    # Add the title.
    plt.title("Age Distribution")

    # Add axis labels.
    plt.xlabel("Age")
    plt.ylabel("Frequency")

    # Display the plot.
    plt.show()


# Plot the fare distribution.
def plot_fare(df):

    # Create a new figure.
    plt.figure(figsize=(8, 5))

    # Create the histogram.
    sns.histplot(df["fare"], bins=30, kde=True)

    # Add the title.
    plt.title("Fare Distribution")

    # Add axis labels.
    plt.xlabel("Fare")
    plt.ylabel("Frequency")

    # Display the plot.
    plt.show()