## Experiment 0: Dataset Setup
- Dataset: Student Dropout & Academic Success (UCI)
- Task: Multi-class classification
- Features: All features
- Target: Target (Dropout, Enrolled, Graduate)


## Experiment 1: Data Inspection
- Rows: 4424
- Columns: 37
- No missing values
- Mixed feature types
- Target: multi-class categorical


## Experiment 3: Column Name Sanitization
- Removed whitespace, symbols, and apostrophes using df.columns
- Ensured API-safe feature names


## Experiment 4: Target Encoding
- Encoded target labels using LabelEncoder from sklearn.preprocessing library
- Classes: Dropout, Enrolled, Graduate
- Preserved encoder for inverse mapping

## Experiment 5: Feature Preprocessing Design
- Classified features by semantic meaning
- Used LightGBM native categorical handling
- No one-hot encoding applied

## Experiment 6: Baseline LightGBM Training
- Model: LGBMClassifier
- Objective: Multi-class
- Estimators: 300
- Learning rate: 0.05
- Stratified 80/20 split

## Experiment 7: Baseline Evaluation
- Accuracy: 77%
- Dropout F1-score: 0.77
- Enrolled F1-score: 0.48
- Graduate F1-score: 0.85
- Observed class overlap for Enrolled category

## Experiment 8: Model Persistence
- Saved trained LightGBM model using joblib
- Saved LabelEncoder for target decoding
- Artifacts stored in `model/` directory
- Enabled model reuse for inference and deployment

## Experiment 9: Scripted Training Pipeline
- Converted notebook-based training into `src/train.py`
- Enabled one-command training using `python -m src.train`
- Resolved package import issues by running in module mode
- Training pipeline is now reproducible and deployment-ready

## Experiment 10: Prediction API (Completed)
- Built FastAPI service for real-time inference (from fastapi import FastAPI)
- Integrated preprocessing and trained LightGBM model
- Exposed `/predict` endpoint returning human-readable predictions
- Successfully tested via Swagger UI 

## Experiment 11: Dockerization
- Installed Docker Desktop and verified setup
- Built Docker image for ML inference API
- Ran container and tested `/predict` endpoint successfully

## Experiment 12: Production Requirements Cleanup
- Identified Docker build failure caused by dev-only and Windows-specific packages
- Replaced pip-freeze requirements with minimal production dependencies
- Successfully rebuilt Docker image with clean requirements

## Experiment 13: LightGBM Runtime Fix
- Docker container crashed due to missing OpenMP library
- Root cause: python:slim image lacks libgomp
- Fixed by installing libgomp1 via apt-get
- LightGBM model loads successfully in Docker

## Experiment 14: Cloud Deployment (Render)
- Deployed Dockerized FastAPI service to Render
- Used Docker runtime with exposed port 8000
- Verified service startup and health
- Public endpoint tested successfully
- Final inference system is live and accessible
