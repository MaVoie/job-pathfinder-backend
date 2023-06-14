from typing import List

from fastapi import APIRouter, status
from pydantic import BaseModel

from model.recruitment_process import RecruitmentProcess
from service.recruitment_process_reader import RecruitmentProcessReader

router = APIRouter()


class SelectedPositionsBody(BaseModel):
    selected_positions: List[str]


@router.post("/processes/{process_id}", response_model=RecruitmentProcess, status_code=status.HTTP_202_ACCEPTED)
async def select_position(process_id: str, selected_position: SelectedPositionsBody):
    return RecruitmentProcessReader.get_recruitment_process()
