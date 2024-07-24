import pickle
import pandas as pd

with open('logistic_regression_model.pkl', 'rb') as file:
    model = pickle.load(file)

def predict_outlier(new_data):
    new_data = pd.DataFrame(new_data, index=[0])
    prediction = model.predict(new_data)
    probability = model.predict_proba(new_data)[:, 1]
    return prediction[0], probability[0]

# insert info
new_data = {'Item ID': '44767',
            'Qty': 500,
            'month': '5',
            'Location ID': '22'}

result, probability = predict_outlier(new_data)
print("1 is the potential outlier:", result)
print("Probability:", probability)


