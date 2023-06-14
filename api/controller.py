from typing import List
from uuid import UUID

from fastapi import APIRouter, status
from pydantic import BaseModel

from service.select_recruitment_positions import SelectRecruitmentPositions

router = APIRouter()
selected_recruitment_positions = SelectRecruitmentPositions()


class SelectedPositionsBody(BaseModel):
    selected_position: str


@router.post("/processes/{process_id}/generate-cover-letters", response_model=str, status_code=status.HTTP_202_ACCEPTED)
async def generate_cover_letter(process_id: UUID, selected_position: SelectedPositionsBody):
    return selected_recruitment_positions.select_recruitment_process_positions(process_id,
                                                                               selected_position.selected_position)
