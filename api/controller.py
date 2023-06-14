import uuid

from fastapi import APIRouter, status

router = APIRouter()


@router.get("/processes/{process_id}", status_code=status.HTTP_202_ACCEPTED)
async def select_position(process_id: str):
    return {"message": f"Hello {process_id}"}
