import os
from langchain import PromptTemplate, LLMChain
from langchain.chat_models import ChatOpenAI
from config import OPENAI_API_KEY
from model.process import Process
from model.user import User

os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY
llm = ChatOpenAI(model_name='gpt-3.5-turbo', temperature=0.9)


class GptService:

    @classmethod
    def generate_cover_letter(cls, process: Process, user: User):
        username = user.name + " " + user.surname
        print(f"input {process.selected_position}, aboutMe {process.custom_msg}")
        prompt = PromptTemplate(
            input_variables=["aboutMe", "position", "username"],
            template="Please generate two cover letters max. 200 words for me for given position: {position}. I have "
                     "introduced "
                     "myself as: {aboutMe}. "
                     "My name is {username}."
                     "If my position does not match my person, just do not generate cover letter.",
        )
        print(prompt.format(aboutMe=process.custom_msg, position=process.selected_position, username=username))
        chain = LLMChain(llm=llm, prompt=prompt)

        return chain.run(aboutMe=process.custom_msg, position=process.selected_position, username=username)

    @classmethod
    def generate_positions(cls, customer_msg: str):
        prompt = PromptTemplate(
            input_variables=["aboutMe"],
            template="I have "
                     "introduced "
                     "myself as: {aboutMe}. "
                     "Please propose for me 5 positions that I should apply for as a pointed list."
        )
        print(prompt.format(aboutMe=customer_msg))
        chain = LLMChain(llm=llm, prompt=prompt)

        return chain.run(aboutMe=customer_msg)