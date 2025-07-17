from sqlalchemy.orm import Session
from backend import models

def save_entry(db: Session, text: str, categories: list):
    entry = models.Entry(text=text)
    db.add(entry)
    db.commit()
    db.refresh(entry)

    for cat in categories:
        activity = models.Activity(entry_id=entry.id, category=cat)
        db.add(activity)
    db.commit()
    return entry

def get_entries(db: Session):
    return db.query(models.Entry).all()

def get_category_counts(db: Session):
    from sqlalchemy import func
    return db.query(models.Activity.category, func.count(models.Activity.id)).group_by(models.Activity.category).all()
