import streamlit as st
import pandas as pd
import pickle
import random

# Load trained model
with open("rf_model.pkl", "rb") as file:
    model = pickle.load(file)

st.title(" Phishing Website Detection System")

st.write("""
This application uses a Random Forest Machine Learning model 
to classify websites as Phishing or Legitimate.
""")

# Load dataset
df = pd.read_csv("data/phishing.csv")
df = df.drop("index", axis=1)
df['Result'] = df['Result'].map({-1: 0, 1: 1})

X = df.drop("Result", axis=1)
y = df["Result"]

st.subheader("Test Model on Random Website")

if st.button("Predict Random Website"):

    random_index = random.randint(0, len(X)-1)
    sample = X.iloc[random_index].values.reshape(1, -1)
    actual_label = y.iloc[random_index]

    prediction = model.predict(sample)[0]

    st.write("### Prediction Result:")

    if prediction == 1:
        st.error("⚠ Predicted: Phishing Website")
    else:
        st.success("Predicted: Legitimate Website")

    st.write("Actual Label:", 
             "Phishing" if actual_label == 1 else "Legitimate")
