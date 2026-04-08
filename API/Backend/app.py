from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import pickle
import numpy as np
import os
import csv

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "best_model.pkl")
csv_path = os.path.join(BASE_DIR, "..", "..", "Dataset", "heart.csv")
html_path = os.path.join(BASE_DIR, "..", "..", "Frontend", "Index.html")

with open(model_path, "rb") as f:
    model = pickle.load(f)["XGBoost"]


class UserInput(BaseModel):
   age:int
   sex:int
   cp:int
   trestbps:int
   chol:int
   fbs:int
   restecg:int
   thalach:int
   exang:int
   oldpeak:float
   slope:int
   ca:int
   thal:int

def save_to_csv(user_input: UserInput, prediction: int):
    file_exists = os.path.exists(csv_path)
    with open(csv_path, mode='a', newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'target'])
        writer.writerow([
            user_input.age,
            user_input.sex,
            user_input.cp,
            user_input.trestbps,
            user_input.chol,
            user_input.fbs,
            user_input.restecg,
            user_input.thalach,
            user_input.exang,
            user_input.oldpeak,
            user_input.slope,
            user_input.ca,
            user_input.thal,
            prediction
        ])



@app.post("/predict")
def predict(user_input: UserInput):
    try:
        input_data = np.array([
            user_input.age,
            user_input.sex,
            user_input.cp,
            user_input.trestbps,
            user_input.chol,
            user_input.fbs,
            user_input.restecg,
            user_input.thalach,
            user_input.exang,
            user_input.oldpeak,
            user_input.slope,
            user_input.ca,
            user_input.thal,
        ]).reshape(1, -1)
        prediction = model.predict(input_data)[0]
        save_to_csv(user_input, prediction)
        return {"prediction": int(prediction)}
    except Exception as e:
        return {"error": str(e)}


@app.get("/", response_class=HTMLResponse)
async def root():
    with open(html_path, "r", encoding="utf-8") as f:
        return f.read()
