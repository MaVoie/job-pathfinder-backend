#controler from fastapi with router
from fastapi import APIRouter, status

from service.recruitment_process_reader import RecruitmentProcessReader

router = APIRouter()


#apply custmomer details
@router.post("/process", status_code=status.HTTP_202_ACCEPTED)
async def apply_customer_details(customer_details: dict):
    return RecruitmentProcessReader.apply_customer_details(customer_details)
