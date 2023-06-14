# controler from fastapi with router
from fastapi import APIRouter, status
import service.process_service as ProcessService
from api.model import user_form, success_create_process, process_response
from uuid import UUID
import logging

router = APIRouter()

@router.post("/processes", status_code=status.HTTP_202_ACCEPTED)
async def apply_customer_details(customer_details: user_form) -> success_create_process:
    uuid = ProcessService.initalize_process(customer_details)
    return success_create_process(id=uuid)


@router.get("/processes/{process_id}/status", status_code=status.HTTP_200_OK)
async def process_details(process_id: UUID) -> process_response:
    logging.warning("dupa")
    return ProcessService.get_process(process_id)
