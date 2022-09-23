import joblib
import os
import json
import logging
import azure.functions as func

TARGET_NAMES = ['setosa', 'versicolor', 'virginica']

def main(req: func.HttpRequest) -> func.HttpResponse:
    model = load_model()
    data = req.get_json()["data"]
    y_pred = model.predict(data)[0]
    pred_class = TARGET_NAMES[y_pred]
    
    logging.info(f"Request: {data} y_pred: {pred_class}")
    response = {"class": pred_class}
    return func.HttpResponse(json.dumps(response))

def load_model():
    path = os.path.join(os.path.dirname(__file__), "model.pkl")
    model = joblib.load(path)
    return model
