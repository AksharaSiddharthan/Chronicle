# backend/schemas.py

from pydantic import BaseModel

class EntryInput(BaseModel):
    text: str
