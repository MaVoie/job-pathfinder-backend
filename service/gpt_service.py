import os
from langchain import PromptTemplate, LLMChain
from langchain.chat_models import ChatOpenAI
from config import OPENAI_API_KEY
from model.recruitment_process import RecruitmentProcess

os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY
llm = ChatOpenAI(model_name='gpt-3.5-turbo', temperature=0)


class GptService:

    @classmethod
    def generate_cover_letter(cls, process: RecruitmentProcess):
        username = process.user.name + " " + process.user.surname
        print(f"input {process.selected_positions}, aboutMe {process.custom_msg}")
        prompt = PromptTemplate(
            input_variables=["aboutMe", "position", "username"],
            template="Please generate two cover letters max. 200 words for me for given position: {position}. I have "
                     "introduced"
                     "myself as: {aboutMe}. "
                     "My name is {username}. If my position does not fit to me, just send me phrase: Consider "
                     "different position to apply for.",
        )
        print(prompt.format(aboutMe=process.custom_msg, position=process.selected_positions[0], username=username))
        chain = LLMChain(llm=llm, prompt=prompt)

        return chain.run(aboutMe=process.custom_msg, position=process.selected_positions[0], username=username)
