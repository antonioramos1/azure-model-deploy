import joblib
import logging
import os
from fastapi import FastAPI, Request


app = FastAPI()
logging.basicConfig(level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S")
LOGGER = logging.getLogger(__name__)


def load_model():
    path = os.path.join(os.path.dirname(__file__), "model.pkl")
    model = joblib.load(path)
    return model


model = load_model()
TARGET_NAMES = ['setosa', 'versicolor', 'virginica']


@app.post("/predict_class")
async def predict_class(request: Request):
    req = await request.json()
    data = req["data"]
    y_pred = model.predict(data)[0]
    pred_class = TARGET_NAMES[y_pred]

    LOGGER.info(f"Request: {data} y_pred: {pred_class}")
    response = {"class": pred_class}
    return response
