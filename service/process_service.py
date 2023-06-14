# write to database
from uuid import uuid4

from model.process import Process
from model.user import User


def create_user_based_on_customer_details(customer_details):
    uuid = uuid4()
    return User(
        id=uuid,
        name=customer_details['name'],
        surname=customer_details['surname'],
        location=customer_details['location'],
        email=customer_details['email']
    )


def createProcess(newCustomerId, param):
    uuid = uuid4()
    return Process(id=uuid,
                   userId=newCustomerId,
                   custom_msg=param)


def initalize_process(customer_details: dict):
    user = create_user_based_on_customer_details(customer_details)
    process = createProcess(user.id, customer_details['custom_msg'])
