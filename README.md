# 🚢 Titanic Survival Prediction API

### End-to-End Machine Learning Project using Python, Scikit-learn & FastAPI

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-orange?logo=scikitlearn)
![FastAPI](https://img.shields.io/badge/FastAPI-API-009688?logo=fastapi)
![License](https://img.shields.io/badge/License-MIT-green)

---

# 📌 Overview

This project is an end-to-end Machine Learning application that predicts whether a passenger survived the Titanic disaster. It demonstrates the complete workflow of a real-world ML project—from data preprocessing and model training to deploying the trained model as a REST API using FastAPI.

The project is organized using a modular structure that follows software engineering best practices, making it easy to maintain, scale, and deploy.

---

# ✨ Features

* 📊 Exploratory Data Analysis (EDA)
* 🧹 Data Cleaning & Preprocessing
* ⚙️ Feature Engineering
* 🤖 Logistic Regression Model
* 📈 Model Evaluation
* 💾 Model Saving with Joblib
* 🚀 FastAPI REST API
* ✅ Input Validation with Pydantic
* 📖 Interactive Swagger Documentation
* 📂 Modular Project Structure
* 🔄 Version Control with Git & GitHub

---

# 🛠️ Technologies Used

| Category          | Tools         |
| ----------------- | ------------- |
| Programming       | Python        |
| Data Analysis     | Pandas, NumPy |
| Machine Learning  | Scikit-learn  |
| Model Persistence | Joblib        |
| API Development   | FastAPI       |
| Data Validation   | Pydantic      |
| API Server        | Uvicorn       |
| Version Control   | Git & GitHub  |

---

# 📂 Project Structure

```text
end-to-end-titanic_project/
│
├── api/
│   ├── __init__.py
│   ├── main.py
│   ├── model_loader.py
│   └── schemas.py
│
├── data/
│   ├── titanic.csv
│   └── clean_titanic.csv
│
├── models/
│   └── model.joblib
│
├── notebooks/
│   └── analysis.ipynb
│
├── src/
│   ├── load_data.py
│   ├── preprocessing.py
│   ├── model.py
│   ├── visualization.py
│   └── utils.py
│
├── README.md
├── requirements.txt
├── .gitignore
└── LICENSE
```

---

# ⚙️ Installation

### Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

### Navigate to the project folder

```bash
cd end-to-end-titanic_project
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the API

Start the FastAPI server:

```bash
uvicorn api.main:app --reload
```

Open your browser:

**Swagger UI**

```
http://127.0.0.1:8000/docs
```

**ReDoc**

```
http://127.0.0.1:8000/redoc
```

---

# 📡 API Endpoint

## POST `/predict`

Predicts whether a passenger survived the Titanic disaster.

### Example Request

```json
{
  "pclass": 3,
  "sex": 0,
  "age": 22,
  "sibsp": 1,
  "parch": 0,
  "fare": 7.25,
  "embarked": 0,
  "alone": 0
}
```

### Example Response

```json
{
  "prediction": "Did Not Survive",
  "prediction_code": 0,
  "confidence": "87.45%"
}
```

---

# 🔄 Machine Learning Workflow

1. Load the Titanic dataset
2. Clean missing values
3. Perform feature engineering
4. Train the Logistic Regression model
5. Evaluate model performance
6. Save the trained model using Joblib
7. Build the FastAPI application
8. Validate inputs using Pydantic
9. Predict survival through a REST API

---

# 🚀 Future Improvements

* Docker Containerization
* Cloud Deployment (AWS/Azure/GCP)
* CI/CD Pipeline
* Unit Testing
* Logging
* Model Versioning
* Authentication & Security

---

# 👨‍💻 Author

**Ahmad Ali**

**Data Scientist | Machine Learning Engineer**

**Skills**

* Python
* Pandas
* NumPy
* Scikit-learn
* FastAPI
* SQL
* Git & GitHub

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

Feedback and suggestions are always welcome!

---

# 📜 License

This project is licensed under the **MIT License**.
