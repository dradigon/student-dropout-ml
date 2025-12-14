# 🎓 Student Dropout Prediction System

An end-to-end **Machine Learning system** that predicts **student academic outcomes** (`Dropout`, `Enrolled`, `Graduate`) using institutional, demographic, and academic data.

This project demonstrates a **production-grade ML workflow**, covering the full lifecycle from data preprocessing to cloud deployment.

---

## 🛠️ Tech Stack

* **Language**: Python
* **Data Processing**: Pandas, NumPy
* **Modeling**: LightGBM, Scikit-learn
* **API**: FastAPI, Pydantic
* **Containerization**: Docker
* **Cloud Deployment**: Render

---

## 📌 Problem Statement

Student dropout is a critical challenge for educational institutions. Early identification of at-risk students enables timely academic intervention.

This system predicts **student academic outcomes** based on historical and institutional data to support data-driven decision making.

---

## 🧠 Machine Learning Details

* **Task**: Multi-class classification
* **Target Classes**:

  * Dropout
  * Enrolled
  * Graduate
* **Model**: LightGBM Classifier
* **Target Encoding**: LabelEncoder
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
│   ├── lgbm_model.pkl        # Trained LightGBM model
│   └── label_encoder.pkl    # Label encoder
│
├── notebooks/
│   └── eda.ipynb             # Exploratory Data Analysis
│
├── src/
│   ├── preprocess.py        # Feature preprocessing
│   └── train.py             # Training pipeline
│
├── experiments.md            # Experiment tracking & decisions
├── Dockerfile                # Docker configuration
├── requirements.txt          # Production dependencies
└── README.md                 # Project documentation
```

---

## 🌐 Live Deployment

The API is deployed and publicly accessible on Render:

* **Base URL**: [https://student-dropout-ml.onrender.com](https://student-dropout-ml.onrender.com)
* **Swagger UI**: [https://student-dropout-ml.onrender.com/docs](https://student-dropout-ml.onrender.com/docs)

---

## 🚀 API Usage

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

## ▶️ Run Locally (Without Docker)

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start API
uvicorn api.main:app --reload
```

Open:

```
http://localhost:8000/docs
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

All experiments, modeling decisions, failures, and production fixes are documented in:

```
experiments.md
```

---

## ⚠️ Model Limitations

* Lower predictive performance for the **Enrolled** class due to class overlap
* Model trained on historical institutional data; generalization may vary across regions
* Predictions are intended to **support** academic decision-making, not replace human judgment

---

## 📌 Future Improvements

* Model monitoring and drift detection
* CI/CD pipeline using GitHub Actions
* Authentication and rate-limiting for API
* Feature importance and explainability (SHAP)

---

## 👤 Author

**Jovan Moris D**
B.Tech Computer Science (AI)
IIITDM Kancheepuram

---

⭐ *This project demonstrates an industry-aligned, end-to-end ML deployment workflow.*
