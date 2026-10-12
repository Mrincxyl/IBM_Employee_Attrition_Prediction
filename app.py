from flask import Flask, render_template, redirect,request
import os, dill
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR/"models"/"attrition_logistic_regression.dill"

with open(MODEL_PATH, "rb") as f:
   model= dill.load(f)
   
FEATURES = [
    "Age",
    "BusinessTravel",
    "Department",
    "DistanceFromHome",
    "Education",
    "EducationField",
    "EnvironmentSatisfaction",
    "Gender",
    "JobInvolvement",
    "JobLevel",
    "JobRole",
    "JobSatisfaction",
    "MaritalStatus",
    "MonthlyIncome",
    "NumCompaniesWorked",
    "OverTime",
    "PercentSalaryHike",
    "PerformanceRating",
    "RelationshipSatisfaction",
    "StockOptionLevel",
    "TotalWorkingYears",
    "TrainingTimesLastYear",
    "WorkLifeBalance",
    "YearsAtCompany",
    "YearsInCurrentRole",
    "YearsSinceLastPromotion",
    "YearsWithCurrManager"
]

NUMERIC_FEATURES = [
    "Age",
    "DistanceFromHome",
    "Education",
    "EnvironmentSatisfaction",
    "JobInvolvement",
    "JobLevel",
    "JobSatisfaction",
    "MonthlyIncome",
    "NumCompaniesWorked",
    "PercentSalaryHike",
    "PerformanceRating",
    "RelationshipSatisfaction",
    "StockOptionLevel",
    "TotalWorkingYears",
    "TrainingTimesLastYear",
    "WorkLifeBalance",
    "YearsAtCompany",
    "YearsInCurrentRole",
    "YearsSinceLastPromotion",
    "YearsWithCurrManager"
] 

CATEGORICAL_OPTIONS = {
    "BusinessTravel": [
        "Travel_Rarely", "Travel_Frequently", "Non-Travel"
    ],
    "Department": [
        "Sales", "Research & Development", "Human Resources"
    ],
    "EducationField": [
        "Life Sciences", "Medical", "Marketing",
        "Technical Degree", "Other", "Human Resources"
    ],
    "Gender": ["Male", "Female"],
    "JobRole": [
        "Sales Executive", "Research Scientist",
        "Laboratory Technician", "Manufacturing Director",
        "Healthcare Representative", "Manager",
        "Sales Representative", "Research Director",
        "Human Resources"
    ],
    "MaritalStatus": ["Single", "Married", "Divorced"],
    "OverTime": ["Yes", "No"]
}  
   
app =   Flask(__name__) 

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/predict",methods=['POST','GET'])
def predict():
    probability = None
    decision = None
    error = None
    if request.method == "POST":
        
        try:
            data = {}
            for feature in FEATURES:
               value = request.form.get(feature,"").strip()
               if not value:
                   raise ValueError(f"Please provide a value for {feature}.")
               if feature in NUMERIC_FEATURES:
                   data[feature] = int(value)
               else:
                   if value not in CATEGORICAL_OPTIONS[feature]:
                       raise ValueError(f"Invalid selection for {feature}.")
                   data[feature] = value
                   
            input_data = pd.DataFrame([data],columns=FEATURES)   
            predicted_class = int(model.predict(input_data)[0])
            probability = float(
                model.predict_proba(input_data)[0,1]
            )
            decision = ("likely to Leave" if predicted_class==1 else "Likely to Stay")
                   
        except (ValueError, TypeError) as exc:
                    error = str(exc)
           
    return render_template("predict.html",features=FEATURES,
            numeric_features=NUMERIC_FEATURES,
            categorical_options=CATEGORICAL_OPTIONS,
            prediction = decision,
            probability=probability,
            error=error
            )


if __name__=="__main__":
    app.run(debug=True)
    