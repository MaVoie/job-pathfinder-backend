from model.recruitment_process import RecruitmentProcess
from model.user import User


class RecruitmentProcessReader:
    @staticmethod
    def get_recruitment_process():
        return RecruitmentProcess(
            user=User(
                id="1",
                name="Hej",
                surname="hej",
                location="Warsaw",
                email="hej@hej.com"
            ),
            id="1",
            custom_msg="Find a job for me!"
        )
