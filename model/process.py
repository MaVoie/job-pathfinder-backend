import pydantic as pydantic
from uuid import UUID


class Process(pydantic.BaseModel):
    id: UUID
    userId: UUID
    custom_msg: str
