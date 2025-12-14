# 🎓 Student Dropout Prediction System

An end-to-end Machine Learning project that predicts **student academic outcomes** (`Dropout`, `Enrolled`, `Graduate`) using institutional, demographic, and academic data.

The project covers the **complete ML lifecycle**:

* Data preprocessing
* Model training (LightGBM)
* API development (FastAPI)
* Docker containerization
* Ready for cloud deployment

---

## 📌 Problem Statement

Student dropout is a critical issue for educational institutions. This project aims to **predict student outcomes early**, enabling timely intervention to improve retention and academic success.

---

## 🧠 Machine Learning Details

* **Task**: Multi-class classification
* **Classes**:

  * Dropout
  * Enrolled
  * Graduate
* **Model**: LightGBM
* **Encoding**: LabelEncoder
* **Evaluation Metrics**:

  * Accuracy
  * Precision
  * Recall
  * F1-score

---

## 🗂️ Project Structure

```
student-dropout-ml/
│
├── api/
│   └── main.py               # FastAPI application
│
├── data/
│   └── students.csv          # Dataset
│
├── model/
│   ├── lgbm_model.pkl        # Trained model
│   └── label_encoder.pkl    # Label encoder
│
├── notebooks/
│   └── eda.ipynb             # Exploratory Data Analysis
│
├── src/
│   ├── preprocess.py        # Feature preprocessing
│   └── train.py             # Model training script
│
├── experiments.md            # Experiment tracking
├── Dockerfile                # Docker configuration
├── requirements.txt          # Dependencies
└── README.md                 # Project documentation
```

---

## 🚀 API Usage

### Base URL

```
http://localhost:8000
```

### Endpoint

```
POST /predict
```

---

### 📥 Sample Request

```json
{
  "Marital_status": 1,
  "Application_mode": 1,
  "Application_order": 1,
  "Course": 9773,
  "Daytime_evening_attendance": 1,
  "Previous_qualification": 1,
  "Previous_qualification_grade": 120,
  "Nacionality": 1,
  "Mothers_qualification": 37,
  "Fathers_qualification": 37,
  "Mothers_occupation": 9,
  "Fathers_occupation": 9,
  "Admission_grade": 130,
  "Displaced": 0,
  "Educational_special_needs": 0,
  "Debtor": 0,
  "Tuition_fees_up_to_date": 1,
  "Gender": 1,
  "Scholarship_holder": 0,
  "Age_at_enrollment": 20,
  "International": 0,
  "Curricular_units_1st_sem_credited": 0,
  "Curricular_units_1st_sem_enrolled": 6,
  "Curricular_units_1st_sem_evaluations": 6,
  "Curricular_units_1st_sem_approved": 6,
  "Curricular_units_1st_sem_grade": 13.5,
  "Curricular_units_1st_sem_without_evaluations": 0,
  "Curricular_units_2nd_sem_credited": 0,
  "Curricular_units_2nd_sem_enrolled": 6,
  "Curricular_units_2nd_sem_evaluations": 6,
  "Curricular_units_2nd_sem_approved": 6,
  "Curricular_units_2nd_sem_grade": 13.0,
  "Curricular_units_2nd_sem_without_evaluations": 0,
  "Unemployment_rate": 12.7,
  "Inflation_rate": 3.7,
  "GDP": 1.7
}
```

---

### 📤 Sample Response

```json
{
  "prediction": "Graduate"
}
```

---

## 🐳 Docker Support

### Build Docker Image

```bash
docker build -t student-dropout-api .
```

### Run Docker Container

```bash
docker run -p 8000:8000 student-dropout-api
```

Then open:

```
http://localhost:8000/docs
```

---

## 🧪 Experiment Tracking

All experiments, model decisions, and observations are documented in:

```
experiments.md
```

---

## 👤 Author

**Jovan Moris D**
B.Tech Computer Science (AI)
IIITDM Kancheepuram

---

## ⭐ Highlights

* End-to-end ML pipeline
* Production-ready API
* Dockerized deployment
* Industry-aligned project structure

---

## 📌 Future Improvements

* Cloud deployment (Render / AWS)
* Model monitoring & drift detection
* CI/CD pipeline
* Authentication for API
