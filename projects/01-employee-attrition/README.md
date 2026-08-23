# Employee Attrition Prediction

## Project Overview
Built a human-centered HR decision-support analysis using the IBM HR Analytics dataset. The project compares classification models, evaluates overtime and workplace factors, and translates model results into retention recommendations while addressing fairness and privacy.

## Dataset
IBM HR Analytics Employee Attrition and Performance; 1,470 employee records and 35 original variables.

## Methods
Logistic Regression, Decision Tree, Random Forest; holdout evaluation with accuracy, precision, recall, F1 and ROC-AUC.

## Key Findings
Overtime was the strongest reported predictor in permutation importance. Logistic Regression provided the strongest recall among the compared models and a useful balance of interpretability and discrimination.

## Business Value
Use predictive analytics for organizational decision support, workload review, retention planning, and targeted investigation—not automated employment decisions.

## Tools
Python, Scikit-learn, HR Analytics

## Repository Contents
This folder contains the primary notebook/report/code artifact used for the portfolio project plus this README. Original course filenames were renamed to clear, employer-facing names.

## Reproducibility
Open the notebook in Jupyter and run cells in order. If a source dataset is not embedded or redistributed, follow the notebook or data-folder note to place the required dataset locally before execution.

## Ethics and Limitations
Model and analytical outputs should be interpreted in context. Results are educational and should support—not replace—human judgment. Data quality, bias, privacy, drift, and the distinction between correlation and causation should be reviewed before real-world use.
