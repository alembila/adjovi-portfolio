# Credit Card Fraud Detection

## Project Overview
Analyzed 339,607 transactions for rare-event fraud detection. Feature engineering and model comparison emphasize precision, recall, F1, ROC-AUC, PR-AUC, and the operational cost of false positives rather than misleading accuracy alone.

## Dataset
Credit-card transaction data with 339,607 records and 1,782 fraudulent transactions (~0.525%).

## Methods
Feature engineering plus Logistic Regression and Random Forest; precision, recall, F1, ROC-AUC, PR-AUC and confusion matrices.

## Key Findings
Fraud patterns differed by transaction amount, category and time; Random Forest captured nonlinear patterns while Logistic Regression remained an interpretable baseline.

## Business Value
Prioritize investigations and tune thresholds to operational capacity while retaining human review.

## Tools
Python, Random Forest, Classification

## Repository Contents
This folder contains the primary notebook/report/code artifact used for the portfolio project plus this README. Original course filenames were renamed to clear, employer-facing names.

## Reproducibility
Open the notebook in Jupyter and run cells in order. If a source dataset is not embedded or redistributed, follow the notebook or data-folder note to place the required dataset locally before execution.

## Ethics and Limitations
Model and analytical outputs should be interpreted in context. Results are educational and should support—not replace—human judgment. Data quality, bias, privacy, drift, and the distinction between correlation and causation should be reviewed before real-world use.
