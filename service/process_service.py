# write to database
from uuid import uuid4
import logging
from api.model import user_form
from model.process import Process
from model.user import User
import repository.process_repository as process_repository
import repository.user_repository as user_repository


def create_user_based_on_customer_details(customer_form: user_form):
    uuid = uuid4()
    return User(
        id=uuid,
        name=customer_form.name,
        surname=customer_form.surname,
        location=customer_form.location,
        email=customer_form.email
    )


def createProcess(newCustomerId, param):
    uuid = uuid4()
    return Process(id=uuid,
                   userId=newCustomerId,
                   custom_msg=param)


def initalize_process(customer_details: user_form):
    user = create_user_based_on_customer_details(customer_details)
    process = createProcess(user.id, customer_details.customer_message)

    user_repository.save(user)
    process_repository.save(process)
    return process.id


def get_process(process_id):
    logging.info("dupa")
    by_id = process_repository.get_by_id(process_id)

    return by_id
