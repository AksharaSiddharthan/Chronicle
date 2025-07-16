# backend/main.py


from fastapi import FastAPI
from schemas import EntryInput
from nlp_engine import predict_categories



app = FastAPI()

@app.post("/predict")
def predict(entry: EntryInput):
    categories = predict_categories(entry.text)
    return {"categories": categories}
