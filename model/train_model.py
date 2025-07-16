from transformers import DistilBertTokenizerFast, DistilBertForSequenceClassification, Trainer, TrainingArguments
from sklearn.preprocessing import MultiLabelBinarizer
from torch.utils.data import Dataset
import torch, os, json

LABELS = ["Nutrition", "Education", "Soul", "Exercise", "Social", "Chores", "Projects"]

# Load data
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

# Tokenize entries
tokenizer = DistilBertTokenizerFast.from_pretrained("distilbert-base-uncased")
X = tokenizer(entries, padding=True, truncation=True, return_tensors="pt")

# Dataset
class JournalDataset(Dataset):
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = torch.tensor(labels, dtype=torch.float32)

    def __getitem__(self, idx):
        item = {k: v[idx] for k, v in self.encodings.items()}
        item["labels"] = self.labels[idx]
        return item

    def __len__(self):
        return len(self.labels)

dataset = JournalDataset(X, y)

# Model
model = DistilBertForSequenceClassification.from_pretrained(
    "distilbert-base-uncased", num_labels=len(LABELS), problem_type="multi_label_classification"
)

# Training args
args = TrainingArguments(
    output_dir="./model_out",
    per_device_train_batch_size=4,
    num_train_epochs=10,
    logging_dir="./logs",
    logging_steps=10,
    save_strategy="epoch"
)

trainer = Trainer(
    model=model,
    args=args,
    train_dataset=dataset,
    tokenizer=tokenizer
)

trainer.train()

# Save model + tokenizer + label encoder
model.save_pretrained("model_out")
tokenizer.save_pretrained("model_out")
with open("model_out/labels.json", "w") as f:
    json.dump(mlb.classes_.tolist(), f)
