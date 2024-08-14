import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import numpy as np

# Load and preprocess data
file_path = 'Check_1.csv'
data = pd.read_csv(file_path)
data['Date'] = pd.to_datetime(data['Date'])
data['month'] = data['Date'].dt.month

features = ['Item ID', 'Qty', 'month', 'Location ID']
X = data[features]
y = data['outlier']

X['Location ID'] = X['Location ID'].astype(str)
X['Item ID'] = X['Item ID'].astype(str)
X['month'] = X['month'].astype(str)
X['Qty'] = X['Qty'].astype(int)

X = X.dropna()
y = y[X.index]

# Balance the dataset
class_0 = X[y == 0].sample(8943, random_state=42)
class_1 = X[y == 1].sample(8943, random_state=42)
X_balanced = pd.concat([class_0, class_1])
y_balanced = pd.concat([pd.Series([0] * 8943), pd.Series([1] * 8943)])

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X_balanced, y_balanced, test_size=0.3, random_state=42)

# Preprocessing and pipeline
numeric_features = ['Qty']
categorical_features = ['Item ID', 'month', 'Location ID']

preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numeric_features),
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
    ])

pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                           ('classifier', LogisticRegression(max_iter=10000))])

# Fit the model
pipeline.fit(X_train, y_train)

# Custom threshold
threshold = 0.5

# Predict probabilities and apply threshold
y_proba = pipeline.predict_proba(X_test)[:, 1]
y_pred = (y_proba >= threshold).astype(int)

# Evaluation
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

print(f"Accuracy: {accuracy}")
print("Classification Report:")
print(report)
print("Confusion Matrix:")
print(conf_matrix)

# Get coefficients and intercept
coefficients = pipeline.named_steps['classifier'].coef_
intercept = pipeline.named_steps['classifier'].intercept_

# Get feature names
feature_names = numeric_features + list(pipeline.named_steps['preprocessor'].named_transformers_['cat'].get_feature_names_out())

import pickle
with open('logistic_regression_model.pkl', 'wb') as file:
    pickle.dump(pipeline, file)