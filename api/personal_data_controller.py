# controler from fastapi with router
from uuid import UUID

from fastapi import APIRouter, status

import service.process_service as ProcessService
from api.model import user_form, success_create_process, process_response
from service.gpt_service import GptService

router = APIRouter()
gpt_service = GptService()


@router.post("/processes", status_code=status.HTTP_202_ACCEPTED)
async def apply_customer_details(customer_details: user_form) -> success_create_process:
    process = ProcessService.initialize_process(customer_details)
    return success_create_process(id=process.id, proposed_positions=process.proposed_positions)


@router.get("/processes/{process_id}/status", status_code=status.HTTP_200_OK)
async def process_details(process_id: UUID) -> process_response:
    return ProcessService.get_process(process_id)
