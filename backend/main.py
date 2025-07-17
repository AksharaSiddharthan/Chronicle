# # backend/main.py
# from fastapi import FastAPI, Depends
# from sqlalchemy.orm import Session
# from backend.schemas import EntryInput, EntryOut
# from backend.db import SessionLocal, engine
# from backend import models, crud
# from backend.nlp_engine import predict_categories

# models.Base.metadata.create_all(bind=engine)

# app = FastAPI()

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# @app.post("/entry", response_model=EntryOut)
# def create_entry(entry: EntryInput, db: Session = Depends(get_db)):
#     categories = predict_categories(entry.text)
#     saved_entry = crud.save_entry(db, entry.text, categories)
#     return {
#         "id": saved_entry.id,
#         "text": saved_entry.text,
#         "created_at": saved_entry.created_at,
#         "categories": categories
#     }

# @app.get("/stats")
# def get_stats(db: Session = Depends(get_db)):
#     counts = crud.get_category_counts(db)
#     return {cat: count for cat, count in counts}

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from backend.schemas import EntryInput, EntryOut
from backend.models import JournalEntry
from backend.database import Base, engine, SessionLocal
from backend.nlp_engine import predict_categories




Base.metadata.create_all(bind=engine)

app = FastAPI()


from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # or your React dev server port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/entry", response_model=EntryOut)
def create_entry(entry: EntryInput, db: Session = Depends(get_db)):
    predicted = predict_categories(entry.text)
    db_entry = JournalEntry(
        text=entry.text,
        categories=",".join(predicted),
    )
    db.add(db_entry)
    db.commit()
    db.refresh(db_entry)
    return {
        "text": db_entry.text,
        "categories": predicted,
        "timestamp": db_entry.timestamp
    }

@app.get("/entries", response_model=list[EntryOut])
def get_entries(db: Session = Depends(get_db)):
    entries = db.query(JournalEntry).all()
    return [
        {
            "text": entry.text,
            "categories": entry.categories.split(","),
            "timestamp": entry.timestamp
        }
        for entry in entries
    ]
