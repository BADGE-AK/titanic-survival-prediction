# 🚢 Titanic Survival Prediction

### End-to-End Machine Learning Project using Python, Scikit-learn, FastAPI & Streamlit

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-orange?logo=scikitlearn)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?logo=fastapi)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-FF4B4B?logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-green)

---

# 📌 Overview

This project is an end-to-end Machine Learning application that predicts whether a passenger survived the Titanic disaster using a **Logistic Regression** model.

The project demonstrates the complete Machine Learning lifecycle, from data preprocessing and feature engineering to model training, evaluation, deployment with **FastAPI**, and an interactive **Streamlit** web application.

The application follows a modular software architecture, separating the Machine Learning model, backend API, and frontend interface to make the project scalable, maintainable, and deployment-ready.

---

# ✨ Features

- 📊 Exploratory Data Analysis (EDA)
- 🧹 Data Cleaning & Preprocessing
- ⚙️ Feature Engineering
- 🤖 Logistic Regression Model
- 📈 Model Evaluation
- 💾 Model Persistence using Joblib
- 🚀 FastAPI REST API
- 🎨 Interactive Streamlit Web Application
- 🔗 Streamlit integrated with FastAPI
- ✅ Input Validation using Pydantic
- 📖 Interactive Swagger API Documentation
- 📂 Modular Project Structure
- 🌐 Ready for Cloud Deployment
- 🔄 Version Control with Git & GitHub

---

# 🛠️ Technologies Used

| Category | Technologies |
|----------|--------------|
| Programming Language | Python |
| Data Analysis | Pandas, NumPy |
| Machine Learning | Scikit-learn |
| Model Persistence | Joblib |
| Backend Framework | FastAPI |
| Frontend Framework | Streamlit |
| Data Validation | Pydantic |
| API Server | Uvicorn |
| Development Tools | Jupyter Notebook, VS Code |
| Version Control | Git & GitHub |

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
│   ├── __init__.py
│   ├── load_data.py
│   ├── preprocessing.py
│   ├── model.py
│   ├── visualization.py
│   └── utils.py
│
├── streamlit_app/
│   ├── app.py
│   ├── api_client.py
│   ├── config.py
│   ├── helpers.py
│   ├── assets/
│   └── pages/
│       ├── Home.py
│       └── About.py
│
├── README.md
├── requirements.txt
├── LICENSE
└── .gitignore
```

---

# 🏗️ Application Architecture

```text
                    User
                      │
                      ▼
        Streamlit Frontend (Port 8501)
                      │
               HTTP POST Request
                      │
                      ▼
         FastAPI Backend (Port 8000)
                      │
                      ▼
      Logistic Regression ML Model
                      │
                      ▼
          Prediction + Confidence
                      │
                      ▼
            Streamlit Displays Result
```

---

# 🔄 Machine Learning Workflow

1. Load the Titanic dataset
2. Perform Exploratory Data Analysis (EDA)
3. Clean and preprocess the data
4. Perform feature engineering
5. Train the Logistic Regression model
6. Evaluate model performance
7. Save the trained model using Joblib
8. Build the FastAPI REST API
9. Validate inputs using Pydantic
10. Develop the Streamlit frontend
11. Connect Streamlit with FastAPI
12. Predict passenger survival through the web application

---

# ⚙️ Installation

## 1. Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

## 2. Navigate to the Project Directory

```bash
cd end-to-end-titanic_project
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🚀 Run the FastAPI Backend

Start the FastAPI server:

```bash
uvicorn api.main:app --reload
```

FastAPI will start on:

```
http://127.0.0.1:8000
```

### Swagger UI

```
http://127.0.0.1:8000/docs
```

### ReDoc Documentation

```
http://127.0.0.1:8000/redoc
```

---

# 🎨 Run the Streamlit Frontend

Start the Streamlit application:

```bash
streamlit run streamlit_app/app.py
```

Open your browser:

```
http://localhost:8501
```

> **Note:** Ensure the FastAPI server is running before using the Streamlit application, as the frontend communicates with the backend API for predictions.

---

# 📡 API Endpoint

## POST `/predict`

Predict whether a passenger survived the Titanic disaster.

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

# 📸 Application Preview

> Screenshots will be added soon.

### Home Page

*Coming Soon*

### Prediction Page

*Coming Soon*

### About Page

*Coming Soon*

### FastAPI Swagger UI

*Coming Soon*

---

# 🚀 Future Improvements

- 🐳 Docker Containerization
- ☁️ Railway Deployment
- ☁️ AWS Deployment
- 🔄 CI/CD with GitHub Actions
- 📊 Model Comparison Dashboard
- 📈 Model Monitoring & Logging
- 🧪 Unit Testing
- 🔐 Authentication & Security

---

# 👨‍💻 Author

## Ahmad Ali

**Data Scientist | Machine Learning Engineer**

### Skills

- Python
- Pandas
- NumPy
- Scikit-learn
- FastAPI
- Streamlit
- SQL
- Git
- GitHub

---

# ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

Feedback, suggestions, and contributions are always welcome!

---

# 📜 License

This project is licensed under the **MIT License**.