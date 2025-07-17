from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import MultiLabelBinarizer
import joblib
import os

LABELS = ["Nutrition", "Education", "Soul", "Exercise", "Social", "Chores", "Projects"]

def load_data(path):
    entries, labels = [], []
    with open(path, "r") as f:
        blocks = f.read().strip().split("\n\n")
        for block in blocks:
            if "Entry:" in block and "Labels:" in block:
                entry = block.split("Entry:")[1].split("Labels:")[0].strip()
                label = block.split("Labels:")[1].strip().split(", ")
                entries.append(entry)
                labels.append([l.strip() for l in label])
    return entries, labels

entries, label_lists = load_data("journal training set.txt")

# Encode labels
mlb = MultiLabelBinarizer(classes=LABELS)
y = mlb.fit_transform(label_lists)

# Vectorize entries
vectorizer = TfidfVectorizer(ngram_range=(1, 2), max_features=1000)
X = vectorizer.fit_transform(entries)

# Train model
model = OneVsRestClassifier(LogisticRegression(solver="liblinear"))
model.fit(X, y)

# Save everything
os.makedirs("model_out", exist_ok=True)
joblib.dump(model, "model_out/sk_model.pkl")
joblib.dump(vectorizer, "model_out/vectorizer.pkl")
joblib.dump(mlb, "model_out/label_binarizer.pkl")

print(" Model, vectorizer, and label encoder saved to model_out/")
