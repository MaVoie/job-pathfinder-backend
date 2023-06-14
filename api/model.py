from pydantic import BaseModel
from uuid import UUID
class user_form(BaseModel):
    name: str
    surname: str
    location: str
    email: str
    customer_message: str


class success_create_process(BaseModel):
    id: UUID


class process_response(BaseModel):
    id: UUID
    userId: UUID
    custom_msg: str