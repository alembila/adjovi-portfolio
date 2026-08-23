"""Employee attrition modeling workflow.
Place the IBM HR Analytics CSV in data/WA_Fn-UseC_-HR-Employee-Attrition.csv before running.
"""
from pathlib import Path
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

DATA = Path(__file__).parent / "data" / "WA_Fn-UseC_-HR-Employee-Attrition.csv"
if not DATA.exists():
    raise FileNotFoundError(f"Dataset not found: {DATA}. See README.md for setup instructions.")

df = pd.read_csv(DATA).drop_duplicates()
y = df["Attrition"].map({"Yes": 1, "No": 0})
X = df.drop(columns=["Attrition", "EmployeeCount", "EmployeeNumber", "Over18", "StandardHours"], errors="ignore")
num_cols = X.select_dtypes(include="number").columns
cat_cols = X.select_dtypes(exclude="number").columns
preprocess = ColumnTransformer([
    ("num", Pipeline([("imputer", SimpleImputer(strategy="median")), ("scale", StandardScaler())]), num_cols),
    ("cat", Pipeline([("imputer", SimpleImputer(strategy="most_frequent")), ("onehot", OneHotEncoder(handle_unknown="ignore"))]), cat_cols),
])
model = Pipeline([("prep", preprocess), ("model", LogisticRegression(max_iter=2000, class_weight="balanced"))])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.20, random_state=42, stratify=y)
model.fit(X_train, y_train)
pred = model.predict(X_test)
proba = model.predict_proba(X_test)[:, 1]
print(classification_report(y_test, pred, digits=3))
print("ROC-AUC:", round(roc_auc_score(y_test, proba), 3))
