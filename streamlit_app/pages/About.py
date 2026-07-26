import streamlit as st

st.title("ℹ️ About This Project")

st.markdown(
    """
## Titanic Survival Prediction

This project predicts whether a passenger survived the Titanic disaster
using a Machine Learning model built with **Scikit-learn**.

### Features

- Predict passenger survival
- FastAPI backend
- Streamlit frontend
- Logistic Regression model

---

### Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- FastAPI
- Streamlit
- Joblib

---

### Model

Algorithm:
- Logistic Regression

Target:
- Survived (1)
- Did Not Survive (0)

---

### Project Structure

Frontend
- Streamlit

Backend
- FastAPI

Machine Learning
- Scikit-learn

---

Developed as an end-to-end Machine Learning project.
"""
)