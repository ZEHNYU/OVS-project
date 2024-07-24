# OVS-project
Outlier detection

**Step 1**
file: Outlier label
Read the Data: Load transaction data from testing.csv into a pandas DataFrame.
Convert Date Column: Convert the 'Date' column to datetime format.
Split Data: Split the DataFrame into two parts, df_before and df_after, based on a specified date (2022-10-07).
Calculate Median Quantity: For both df_before and df_after, calculate the median quantity for each 'Item ID' and add it as a new column 'Median_Qty'.
Calculate Quantity Minus Median: Add a new column 'Qty_Minus_Median' to both df_before and df_after, representing the difference between the quantity and its median.
Calculate Maximum Difference: Calculate the maximum value of 'Qty_Minus_Median' for each 'Item ID' in df_after and store these values in a dictionary.
Adjust Quantity Minus Median: Create a new column 'Adjusted_Qty_Minus_Median' in df_before, adjusted by subtracting the maximum 'Qty_Minus_Median' from the dictionary.
Save Results: Save the modified df_before DataFrame to a new CSV file, 'Check_1.csv'.

**Step 2**
file: outlier logistic2
Load and Preprocess Data: Load transaction data from merged_file.csv, convert 'Date' to datetime, and extract the month. Define features and the target variable.
Data Preparation: Convert categorical features to strings, drop missing values, and balance the dataset by sampling equal numbers of outlier and non-outlier classes.
Split Data: Split the balanced data into training and testing sets.
Preprocessing and Pipeline Setup: Create a preprocessing pipeline that standardizes numerical features and one-hot encodes categorical features. Combine preprocessing with a logistic regression classifier in a pipeline.
Model Training: Fit the logistic regression model using the training data.
Custom Threshold for Prediction: Set a threshold for predicting outliers and apply it to predicted probabilities.
Model Evaluation: Evaluate the model's performance using accuracy score, classification report, and confusion matrix.
Logistic Regression Equation: Retrieve and print the logistic regression equation, including coefficients and intercepts.
Save the Model: Save the trained logistic regression model to a file named logistic_regression_model.pkl using pickle.


**Step 3**
file" logistic model

Load the Model: Load a pre-trained logistic regression model from logistic_regression_model.pkl using pickle.
Define Prediction Function: Define a function predict_outlier that:
Accepts new data as input.
Converts the input data to a pandas DataFrame.
Uses the loaded model to predict whether the new data is an outlier.
Returns the prediction and the associated probability.
Predict on New Data: Define a sample new data dictionary, call the predict_outlier function with this data, and print the prediction and probability.
