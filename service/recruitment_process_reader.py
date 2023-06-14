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
            custom_msg="I'm 20 years old. Need to find a job as java junior developer. Do not have any experience, but "
                       "I graduated from Warsaw University of Technology with bachelor's degree from Java 17. I have "
                       " Oracle"
                       " Certificate from java 17 as well.",
            selected_positions=["Java Developer"]
        )
