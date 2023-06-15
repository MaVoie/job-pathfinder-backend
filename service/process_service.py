# write to database
from uuid import uuid4

from click import UUID

import repository.process_repository as process_repository
import repository.user_repository as user_repository
from job_api.model import user_form
from model.process import Process
from model.user import User
from service.gpt_service import GptService

gpt_service = GptService()


def create_user_based_on_customer_details(customer_form: user_form):
    uuid = uuid4()
    return User(
        id=uuid,
        name=customer_form.name,
        surname=customer_form.surname,
        location=customer_form.location,
        email=customer_form.email
    )


def createProcess(newCustomerId, param, generated_positions):
    uuid = uuid4()
    return Process(id=uuid,
                   userId=newCustomerId,
                   custom_msg=param,
                   proposed_positions=generated_positions
                   )


def initialize_process(customer_details: user_form):
    user = create_user_based_on_customer_details(customer_details)
    generated_positions = gpt_service.generate_positions(customer_details.customer_message)
    process = createProcess(user.id, customer_details.customer_message, generated_positions)

    user_repository.save(user)
    process_repository.save(process)
    return process


def generate_interview_questions(process_id: UUID):
    process = get_process(process_id)
    questions = gpt_service.generate_interview_questions(process)
    process.interview_questions = questions
    process_repository.save(process)
    return questions


def validate_interview_question(process_id: UUID, question: str, answer: str):
    process = get_process(process_id)
    return gpt_service.validate_interview_question_answer(process, question, answer)


def get_process(process_id):
    by_id = process_repository.get_by_id(process_id)
    return by_id
