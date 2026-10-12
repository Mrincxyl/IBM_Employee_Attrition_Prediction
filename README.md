# AttritionIQ — Employee Attrition Prediction

A machine learning web application that predicts employee attrition using Logistic Regression and the IBM HR Analytics Employee Attrition & Performance dataset. The project combines exploratory data analysis (EDA), data preprocessing, model training, and a Flask-based web interface.

## Overview

Employee attrition occurs when employees leave an organization. Understanding patterns associated with attrition can help organizations investigate workforce trends and identify areas that may require further analysis.

AttritionIQ accepts employee-related information and returns a predicted class — **Likely to Stay** or **Likely to Leave** — along with the model's estimated probability of attrition.

This project is intended for learning, experimentation, and educational demonstration. Predictions are estimates, not guarantees about individual employees.

## Features

- **Exploratory Data Analysis:** Analyze employee demographics, job roles, satisfaction, compensation, tenure, and attrition patterns.
- **Data Preprocessing:** Handle categorical and numerical features using a machine learning preprocessing pipeline.
- **Feature Selection:** Exclude identifier and constant columns, along with selected rate-related features.
- **Logistic Regression:** Train a binary classification model to predict the `Attrition` target.
- **Model Persistence:** Save and load the trained pipeline using Dill.
- **Flask Web Application:** Provide a web interface for entering employee information and viewing predictions.
- **Prediction Probability:** Display the model's estimated probability for the attrition class.
- **Responsive Interface:** Use HTML and CSS to provide a professional, responsive user experience.

## Technology Stack

| Category | Technologies |
|---|---|
| Programming language | Python |
| Data analysis | Pandas, NumPy |
| Data visualization | Matplotlib, Seaborn |
| Machine learning | Scikit-learn |
| Model serialization | Dill |
| Backend | Flask |
| Frontend | HTML5, CSS3 |
| Development environment | Jupyter Notebook, VS Code |
| Version control | Git, GitHub |

## Dataset

**Dataset:** IBM HR Analytics Employee Attrition & Performance

The dataset contains **1,470 employee records and 35 columns**, including employee-related attributes and the target variable `Attrition`.

- **Target variable:** `Attrition`
- **Classification task:** Binary classification
- **Classes:** `Yes` (left) and `No` (stayed)
- **Original target distribution:** 237 employees with `Yes` and 1,233 with `No`

The original dataset is imbalanced, so model evaluation should consider precision, recall, F1-score, and ROC-AUC rather than accuracy alone.

The project excludes non-predictive identifier or constant columns and removes selected rate-related features based on exploratory analysis and cross-validation comparison.

## Project Structure

```text
IBM_Attrition_Project/
│
├── app.py
├── models/
│   └── attrition_logistic_regression.dill
│
├── notebooks/
│   ├── eda.ipynb
│   ├── model_training.ipynb
│   └── data/
│       └── WA_Fn-UseC_-HR-Employee-Attrition.csv
│
├── templates/
│   ├── home.html
│   └── index.html
│
├── static/
│   └── style.css
│
├── requirements.txt
├── README.md
└── .gitignore
```

*The structure above is illustrative. Adjust notebook, dataset, or model filenames if yours differ.*

## Machine Learning Workflow

Follow this order for a typical classification problem using Logistic Regression.
### 1. Load the dataset
Understand rows, columns and target


### 2. Initial data inspection and EDA
Data types, missing values, duplicates, distributions and relationships


### 3. Train-test split
Separate training and unseen testing data


### 4. Feature Engineering and Feature Selection
Define useful features using training data; avoid target leakage


### 5. Missing-value imputation
Learn fill values from training data


### 6. One-Hot Encoding
Convert nominal categorical features into numeric columns


### 7. StandardScaler
Scale appropriate numerical features


### 8. Train Logistic Regression
Learn patterns from processed training data


### 9. Evaluate on test data
Precision, recall, F1-score, confusion matrix and ROC-AUC

Because employees who leave represent the minority class, recall for `Attrition = Yes` is particularly important. A high accuracy score alone does not mean that the model reliably identifies employees who leave.

### 10. Model Saving

The trained pipeline is serialized to a `.dill` file in the main project's `models/` directory. Flask loads this saved pipeline to make predictions on new input data.

## Installation and Setup

### Prerequisites

- Python 3.10 or a compatible Python version.
- pip
- Git (optional, for cloning the repository).

### 1. Clone the repository

```bash
git clone https://github.com/Mrincxyl/IBM_Employee_Attrition_Prediction
cd IBM_Attrition_Project
```

Alternatively, download the project and open its root folder in VS Code.

### 2. Create a virtual environment

**Windows PowerShell:**

```cmd
conda create -n attrition_env python=3.12 -y
conda activate attrition_env
```

If cmd blocks environment activation, use the appropriate activation method for your terminal.

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Check the model file

The saved model exists at:

```text
models/attrition_logistic_regression.dill
```



### 5. Run the Flask application

From the project root directory, execute:

```bash
python app.py
```

Open the local address shown in the terminal, usually:

```text
http://127.0.0.1:5000/
```

The home page introduces the project. Select the prediction option to open the employee information form.

## Using the Application

1. Open the home page.
2. Review the project overview and feature descriptions.
3. Navigate to the prediction form.
4. Enter the required employee information.
5. Submit the form.
6. Review the predicted class and estimated attrition probability.

The input fields must match the feature names and conventions used during model training.

## Responsible Use and Limitations

- A prediction does not establish whether an employee will actually leave.
- Historical relationships do not necessarily represent causation.
- Model performance may change when applied to another organization or population.
- The dataset may contain historical biases and limitations.
- Predicted probabilities may not be perfectly calibrated.
- Employee information should be handled with appropriate privacy and security safeguards.

This educational prototype should not be used as the sole basis for hiring, firing, promotion, compensation, or other consequential employment decisions.

## Future Improvements

Potential extensions include:

- Comparing Logistic Regression with tree-based classification models.
- Improving minority-class recall through carefully validated techniques.
- Adding model interpretability with SHAP or other suitable methods.
- Monitoring model performance and data drift.
- Deploying the application to a cloud platform.
- Adding automated tests and a reproducible training workflow.

## Author

**SK Raihan Ali**

- **GitHub:** [Mrincxyl](https://github.com/Mrincxyl)
- **LinkedIn:** [SK Raihan Ali](https://www.linkedin.com/in/raihanxsk/)

Developed as a machine learning project focused on employee attrition analysis, predictive modeling, and Flask web application development.

## Live Demo

https://ibm-employee-attrition-prediction.onrender.com/

## License

Choose and add an appropriate open-source license before distributing this project publicly. Check the dataset's applicable terms separately.

---

**Disclaimer:** This project is intended for educational and analytical purposes. Predictions should be interpreted cautiously and should not be treated as definitive assessments of individual employees.
