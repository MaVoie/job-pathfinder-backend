from typing import List

from fastapi import APIRouter, status
from pydantic import BaseModel

from model.recruitment_process import RecruitmentProcess
from service.select_recruitment_positions import SelectRecruitmentPositions

router = APIRouter()
selected_recruitment_positions = SelectRecruitmentPositions()


class SelectedPositionsBody(BaseModel):
    selected_positions: List[str]


@router.post("/processes/{process_id}", response_model=str, status_code=status.HTTP_202_ACCEPTED)
async def generate_cover_letter(process_id: str, selected_position: SelectedPositionsBody):
    return selected_recruitment_positions.select_recruitment_process_positions(process_id,
                                                                               selected_position.selected_positions)
