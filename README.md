# US Job Postings Classification

This project uses a logistic regression model to classify job postings based on their textual content.

## Dataset
The dataset used for training the model can be found [here](https://www.kaggle.com/datasets/techmap/us-job-postings-from-2023-05-05).

## How to Run

1. Clone this repository.

```
git clone https://github.com/younestr/NLP-JobPostings.git
```
For the streamlit app version : 

   1. Run the Streamlit app:
```
streamlit run app.py
```
   2. Enter a job posting description in the text box and click "Classify" to get the prediction.

For the react app version : 

   1. Go to the backend directory and start it :
```
cd react_backend
python main.py
```
   2. Go to the react application directory and start it :
```
cd react-app
npm start
```
   3. Enter a job posting description in the text box and click "Classify" to get the prediction.

