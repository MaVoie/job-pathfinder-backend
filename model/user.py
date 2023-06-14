from pydantic import BaseModel
from uuid import UUID


class User(BaseModel):
    id: UUID
    name: str
    surname: str
    location: str
    email: str
