from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from .database import Base # type: ignore

class JournalEntry(Base):
    __tablename__ = "entries"

    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=False)
    categories = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
