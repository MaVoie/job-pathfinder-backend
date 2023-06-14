import pydantic as pydantic

from model.user import User


class Process(pydantic.BaseModel):
    id: str
    userId: str
    custom_msg: str
