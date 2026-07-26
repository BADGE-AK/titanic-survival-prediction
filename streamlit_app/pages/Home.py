import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

import streamlit as st

from api_client import predict_passenger
from helpers import (
    encode_sex,
    encode_embarked,
    encode_alone
)

# ---------------------------------
# Page Title
# ---------------------------------

st.title("🚢 Passenger Information")

st.write(
    "Fill in the passenger details and click **Predict**."
)

# ---------------------------------
# Passenger Class
# ---------------------------------

pclass = st.selectbox(
    "Passenger Class",
    [1, 2, 3]
)

# ---------------------------------
# Gender
# ---------------------------------

sex = st.selectbox(
    "Sex",
    ["Male", "Female"]
)

# ---------------------------------
# Age
# ---------------------------------

age = st.number_input(
    "Age",
    min_value=0,
    max_value=100,
    value=25
)

# ---------------------------------
# Siblings / Spouses
# ---------------------------------

sibsp = st.number_input(
    "Siblings / Spouses",
    min_value=0,
    value=0
)

# ---------------------------------
# Parents / Children
# ---------------------------------

parch = st.number_input(
    "Parents / Children",
    min_value=0,
    value=0
)

# ---------------------------------
# Fare
# ---------------------------------

fare = st.number_input(
    "Fare",
    min_value=0.0,
    value=32.20
)

# ---------------------------------
# Embarked
# ---------------------------------

embarked = st.selectbox(
    "Embarked",
    [
        "Southampton",
        "Cherbourg",
        "Queenstown"
    ]
)

# ---------------------------------
# Alone
# ---------------------------------

alone = st.radio(
    "Travelling Alone?",
    [
        "Yes",
        "No"
    ]
)

# ---------------------------------
# Predict Button
# ---------------------------------

if st.button("Predict"):

    passenger = {

        "pclass": pclass,

        "sex": encode_sex(sex),

        "age": age,

        "sibsp": sibsp,

        "parch": parch,

        "fare": fare,

        "embarked": encode_embarked(embarked),

        "alone": encode_alone(alone)
    }

    result = predict_passenger(passenger)

    if "error" in result:

        st.error(result["error"])

    else:

        st.success(
            f"Prediction: {result['prediction']}"
        )

        st.info(
            f"Confidence: {result['confidence']}"
        )