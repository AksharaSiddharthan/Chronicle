# # backend/schemas.py

# from pydantic import BaseModel
# from typing import List
# from datetime import datetime

# class EntryInput(BaseModel):
#     text: str



# class EntryOut(BaseModel):
#     id: int
#     text: str
#     created_at: datetime
#     categories: List[str]

#     class Config:
#         "from_attributes" == True

from pydantic import BaseModel
from datetime import datetime
from typing import List

class EntryInput(BaseModel):
    text: str

class EntryOut(BaseModel):
    text: str
    categories: List[str]
    timestamp: datetime
