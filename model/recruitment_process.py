from typing import List, Optional

from pydantic import BaseModel

from model.user import User


class RecruitmentProcess(BaseModel):
    user: User
    id: str
    custom_msg: str
    selected_positions: List[str]
