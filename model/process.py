from typing import List, Optional

import pydantic as pydantic
from uuid import UUID


class Process(pydantic.BaseModel):
    id: UUID
    userId: UUID
    custom_msg: str
    proposed_positions: str
    selected_position: Optional[str] = None
    covered_letters: Optional[List[str]] = None
