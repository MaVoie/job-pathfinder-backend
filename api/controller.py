
from fastapi import APIRouter, status

from service.recruitment_process_reader import RecruitmentProcessReader

router = APIRouter()


@router.get("/processes/{process_id}", status_code=status.HTTP_202_ACCEPTED)
async def select_position(process_id: str, selected_position: str):
    return RecruitmentProcessReader.get_recruitment_process()
