# AutoJudge – Problem Difficulty Prediction System
## Overview 
AutoJudge is a machine learning–based system that predicts the difficulty level (Easy / Medium / Hard) and a numerical difficulty score of programming problems using their textual descriptions. The project combines Natural Language Processing (NLP), classification, regression, and a web-based interface for real-time predictions.
## Approach
1. Data Preprocessing
- Combined multiple text fields:
  - Problem Description
  - Input Description
  - Output Description
- Cleaned text by:
  - Removing line breaks and extra spaces
  - Converting text to lowercase
  - Removing stopwords
  - Tokenization and lemmatization
- Encoded categorical target labels using Label Encoding
- Standardized numerical features for the regression task
- Verified that the dataset contains no missing values
2. Feature Engineering
- Used TF-IDF Vectorization to convert text into numerical features
- Considered unigrams and bigrams to capture contextual meaning
- Limited feature size to control sparsity and overfitting
## Models Used

1. Classification (Problem Difficulty)
  - Logistic Regression (baseline)
  - XGBoost Classifier (final choice)
  - Reason for choosing XGBoost:
    - Handles high-dimensional sparse TF-IDF features better
    - Captures non-linear relationships
    - Provided better recall and overall performance than Logistic Regression
- Final Classification Results (XGBoost):
  - Accuracy: 0.54
  - Performance varied across classes, reflecting the subjective nature of difficulty labeling
2. Regression (Difficulty Score)
- Predicts a continuous difficulty score
- Evaluated using:
  - Mean Absolute Error (MAE)
  - Root Mean Squared Error (RMSE)
- Final Regression Results:
  - MAE: 1.68
  - RMSE: 2.02

These results indicate reasonable prediction accuracy given the variability in problem difficulty.

3. Model Deployment 
- Exported trained pipelines using joblib
- Integrated both classification and regression models into a Flask backend
## Web Interface 
- Built using Flask + HTML + CSS
- Users can input:
  - Problem Description
  - Input Description
  - Output Description
- The system displays:
  - Predicted Difficulty Class (Easy / Medium / Hard)
  - Predicted Difficulty Score

## Project Structure

```
Submission/
│
├── app.py
├── requirements.txt
│
├── models/
│   ├── difficulty_classifier.pkl
│   ├── difficulty_regressor.pkl
│   └── label_encoder.pkl
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

Requirements

- Python 3.10+
- Flask
- scikit-learn
- xgboost
- numpy
- pandas
- joblib

(All dependencies are listed in requirements.txt)

## Setup Instructions (Run Locally)
1. Clone the reopsitory 
```bash
git clone https://github.com/Aditibharadwaj/AutoJudge.git
cd AutoJudge
```
2. Install dependencies
```bash
pip install -r requirements.txt
```
3. Run the Flask application
```bash
python app.py
```
4. Open in the browser
```cpp
http://127.0.0.1:5000
```

Author 

Aditi B R

23113009







