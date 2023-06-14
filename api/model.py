from typing import List, Optional

from pydantic import BaseModel
from uuid import UUID


class user_form(BaseModel):
    name: str
    surname: str
    location: str
    email: str
    customer_message: str


class success_create_process(BaseModel):
    process_id: UUID
    proposed_positions: List[str]


class interview_questions(BaseModel):
    questions: List[str]


class interview_question_evaluation(BaseModel):
    evaluation: str


class process_response(BaseModel):
    id: UUID
    userId: UUID
    custom_msg: str
    proposed_positions: Optional[List[str]] = None
    interview_questions: Optional[List[str]] = None
    covered_letters: Optional[List[str]] = None
