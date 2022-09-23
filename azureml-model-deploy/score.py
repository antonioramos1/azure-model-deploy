import os
import joblib
import json


TARGET_NAMES = ['setosa', 'versicolor', 'virginica']


def init():
    global model
    model_path = os.path.join(os.getenv('AZUREML_MODEL_DIR'), 'model.pkl')
    model = joblib.load(model_path)

def run(raw_data):
    data = json.loads(raw_data)["data"]
    y_pred = model.predict(data)[0]
    pred_class = TARGET_NAMES[y_pred]

    print(f"Request: {data} y_pred: {pred_class}")
    response = {"class": pred_class}
    return response
