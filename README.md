# Phishing Website Detection System

##  Overview
This project implements a Machine Learning-based system to detect phishing websites using security-related URL features. 

Phishing is one of the most common cyber security threats where attackers create fake websites to steal user credentials such as passwords, banking details, and personal data.

This system uses supervised machine learning algorithms to classify websites as either:

- 0 → Legitimate
- 1 → Phishing


##  Problem Statement
To build a classification model that can automatically detect phishing websites based on extracted URL and domain features, thereby helping prevent cyber attacks and data theft.

---

##  Dataset Description
- Total Samples: 11,055 websites
- Total Features: 30 security-related features
- Target Column: `Result`
  - 0 → Legitimate Website
  - 1 → Phishing Website

### Example Features:
- URL Length
- Having IP Address
- SSL Final State
- Domain Registration Length
- Google Index
- Page Rank
- Age of Domain


## Machine Learning Models Used

### 1️ Logistic Regression
- Accuracy: 92.44%
- Baseline classification model

### 2 Random Forest Classifier
- Accuracy: 96.65%
- Reduced false negatives significantly
- Selected as final deployed model

Random Forest performed better due to ensemble learning and better handling of feature interactions.


##  Model Evaluation

Evaluation metrics used:
- Accuracy
- Confusion Matrix
- Precision
- Recall

Random Forest reduced phishing misclassification compared to Logistic Regression.


## Application Deployment

The trained Random Forest model is deployed using Streamlit to provide a simple interactive interface.

Users can:
- Test the model using a random website sample
- View prediction results instantly


## Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Streamlit



