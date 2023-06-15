from typing import List
from uuid import UUID

from fastapi import APIRouter, status
from pydantic import BaseModel

from service.select_recruitment_positions import SelectRecruitmentPositions
from service.process_service import generate_interview_questions, validate_interview_question
from .model import interview_questions, interview_question_evaluation

router = APIRouter()
selected_recruitment_positions = SelectRecruitmentPositions()


class SelectedPositionsBody(BaseModel):
    selected_position: str


class QuestionAnswerBody(BaseModel):
    question: str
    answer: str


@router.post("/processes/{process_id}/generate-cover-letters", response_model=List[str],
             status_code=status.HTTP_202_ACCEPTED)
async def generate_cover_letter(process_id: UUID, selected_position: SelectedPositionsBody):
    return selected_recruitment_positions.select_recruitment_process_positions(process_id,
                                                                               selected_position.selected_position)


@router.get("/processes/{process_id}/interview-questions",
            status_code=status.HTTP_202_ACCEPTED)
async def generate_cover_letter(process_id: UUID) -> interview_questions:
    return interview_questions(questions=generate_interview_questions(process_id))


@router.post("/processes/{process_id}/interview-questions-answer",
             response_model=str,
             status_code=status.HTTP_202_ACCEPTED)
async def generate_cover_letter(process_id: UUID, body: QuestionAnswerBody) -> interview_question_evaluation:
    response = validate_interview_question(process_id, body.question, body.answer)
    return interview_question_evaluation(evaluation=response)
