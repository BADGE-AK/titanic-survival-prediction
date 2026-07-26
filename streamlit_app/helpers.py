"""
Helper functions for Streamlit.
"""


def encode_sex(sex: str) -> int:
    """
    Convert gender into the value expected by the model.

    Male   -> 1
    Female -> 0
    """

    mapping = {
        "Male": 1,
        "Female": 0
    }

    return mapping[sex]


def encode_embarked(port: str) -> int:
    """
    Convert embarkation port into numeric values.

    Southampton -> 0
    Cherbourg   -> 1
    Queenstown  -> 2
    """

    mapping = {
        "Southampton": 0,
        "Cherbourg": 1,
        "Queenstown": 2
    }

    return mapping[port]


def encode_alone(alone: str) -> int:
    """
    Convert travelling alone option.

    Yes -> 1
    No  -> 0
    """

    mapping = {
        "Yes": 1,
        "No": 0
    }

    return mapping[alone]