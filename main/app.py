import streamlit as st
import joblib

# Load your model and the correct vectorizer
model = joblib.load(r'C:\Users\hp\Downloads\NLP-JobPostings\model\logistic_regression_model.joblib')
tfidf_vectorizer = joblib.load(r'C:\Users\hp\Downloads\NLP-JobPostings\model\tfidf_vectorizer.joblib')

# Define the Streamlit interface
st.title("Job Postings Classification Interface")
st.write("Enter the job posting text and see the classification.")

# Get user input
user_input = st.text_area("Job Posting Text:")

# Classify the input when the button is clicked
if st.button("Classify"):
    if user_input:
        # Transform user input with TF-IDF
        input_transformed = tfidf_vectorizer.transform([user_input])  # Use transform() not fit_transform()
        
        # Predict the label
        prediction = model.predict(input_transformed)
        
        # Display the result
        st.write(f"Predicted Label: {prediction[0]}")
    else:
        st.write("Please enter some text to classify.")
