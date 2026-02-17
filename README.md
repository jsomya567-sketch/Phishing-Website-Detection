# Phishing Website Detection System

## Overview
This project implements a Machine Learning-based system to detect phishing websites using security-related URL features.

## Problem Statement
Phishing websites attempt to steal sensitive information by mimicking legitimate websites. This project builds a classification model to automatically detect phishing websites.

## Dataset
- 11,055 website samples
- 30 security-related features
- Target column: Result (0 = Legitimate, 1 = Phishing)

## Models Used
1. Logistic Regression
2. Random Forest Classifier

## Results
- Logistic Regression Accuracy: 92.44%
- Random Forest Accuracy: 96.65%

Random Forest performed better and significantly reduced false negatives.

## Technologies Used
- Python
- Pandas
- Scikit-learn
- Streamlit
- Matplotlib
- Seaborn

## How to Run
1. Install dependencies:
   pip install -r requirements.txt

2. Run the application:
   streamlit run app.py
