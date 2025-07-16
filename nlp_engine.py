# backend/nlp_engine.py

import torch
import json
from transformers import DistilBertForSequenceClassification, DistilBertTokenizerFast

# Load model and tokenizer
MODEL_PATH = "../model/model_out"
model = DistilBertForSequenceClassification.from_pretrained(MODEL_PATH)
tokenizer = DistilBertTokenizerFast.from_pretrained(MODEL_PATH)
model.eval()

# Load labels
with open(f"{MODEL_PATH}/labels.json", "r") as f:
    LABELS = json.load(f)

def predict_categories(text: str):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        logits = model(**inputs).logits
        probs = torch.sigmoid(logits).squeeze().numpy()

    predictions = [LABELS[i] for i, p in enumerate(probs) if p > 0.5]
    return predictions
