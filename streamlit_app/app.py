"""
Main entry point for the Streamlit application.
"""

import streamlit as st

from config import (
    APP_TITLE,
    PAGE_ICON,
    LAYOUT
)


# ----------------------------------------
# Configure the page
# ----------------------------------------

st.set_page_config(
    page_title=APP_TITLE,
    page_icon=PAGE_ICON,
    layout=LAYOUT
)


# ----------------------------------------
# Sidebar
# ----------------------------------------

st.sidebar.title("Navigation")

st.sidebar.success(
    "Select a page from the sidebar."
)


# ----------------------------------------
# Main Page
# ----------------------------------------

st.title("🚢 Titanic Survival Prediction")

st.write(
    """
    Welcome to the Titanic Survival Prediction App.

    Use the navigation menu on the left to access the prediction page.
    """
)


st.info(
    """
    This application uses a Logistic Regression model
    served by a FastAPI backend.
    """
)