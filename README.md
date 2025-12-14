# 🎓 Student Dropout Prediction System

An end-to-end Machine Learning project to predict student outcomes  
(**Dropout / Enrolled / Graduate**) using academic, demographic, and economic features.

---

## 📌 Problem Statement
Student dropout is a major challenge in higher education.  
Early prediction helps institutions provide timely interventions.

This project builds a **multi-class classification model** and exposes it via a **production-ready API**.

---

## 📊 Dataset
- Source: UCI Machine Learning Repository
- Records: 4,424 students
- Features: 36
- Target classes:
  - Dropout
  - Enrolled
  - Graduate

---

## 🧠 Model
- Algorithm: **LightGBM**
- Task: Multi-class classification
- Evaluation Metrics:
  - Accuracy
  - Precision, Recall, F1-score

---

## ⚙️ Project Structure

student-dropout-ml/
├── api/ # FastAPI application
├── src/ # Training & preprocessing logic
├── model/ # Saved ML artifacts
├── data/ # Dataset (training only)
├── notebooks/ # EDA & experiments
├── experiments.md # Experiment tracking
├── Dockerfile # Containerization
└── requirements.txt


---

## 🚀 API Usage

### Endpoint

### Sample Request

POST/predict

```json
{
  "Marital_status": 1,
  "Application_mode": 1,
  "Course": 9773,
  "Age_at_enrollment": 20,
  "Curricular_units_1st_sem_approved": 6,
  "Curricular_units_2nd_sem_approved": 6,
  "GDP": 1.7
}


Sample Response
{
  "prediction": "Graduate"
}

🐳 Docker Support

Build image:

docker build -t student-dropout-api .


Run container:

docker run -p 8000:8000 student-dropout-api

🧪 Experiment Tracking

All experiments and decisions are documented in experiments.md.

👤 Author

Jovan Moris D
B.Tech Computer Science (AI)