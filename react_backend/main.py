from flask import Flask, request, jsonify
import joblib
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # To handle CORS issues when making requests from React

# Load the logistic regression model and the TF-IDF vectorizer
model = joblib.load(r'C:\Users\hp\Downloads\NLP-JobPostings\model\logistic_regression_model.joblib')
tfidf_vectorizer = joblib.load(r'C:\Users\hp\Downloads\NLP-JobPostings\model\tfidf_vectorizer.joblib')

@app.route('/classify', methods=['POST'])
def classify():
    data = request.json
    text = data['text']  # Extract the text from the request

    # Transform the input text with the TF-IDF vectorizer
    text_transformed = tfidf_vectorizer.transform([text])

    # Make the prediction using the logistic regression model
    prediction = model.predict(text_transformed)

    # Return the prediction as a JSON response
    return jsonify({'prediction': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
