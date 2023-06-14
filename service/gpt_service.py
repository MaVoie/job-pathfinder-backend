import os
from langchain import PromptTemplate, LLMChain
from langchain.chat_models import ChatOpenAI
from config import OPENAI_API_KEY, OPENAI_ORGANIZATION
from model.process import Process
from model.user import User

os.environ['OPENAI_API_KEY'] = OPENAI_API_KEY
os.environ['OPENAI_ORGANIZATION'] = OPENAI_ORGANIZATION
llm = ChatOpenAI(model_name='gpt-4', temperature=0)


class GptService:

    @classmethod
    def generate_cover_letter(cls, process: Process, user: User):
        username = user.name + " " + user.surname
        print(f"input {process.selected_position}, aboutMe {process.custom_msg}")
        prompt = PromptTemplate(
            input_variables=["aboutMe", "position", "username"],
            template="""
            Please generate two cover letters 400-500 words for me for given position: {position}.
            I do not have any experience in that field.
            Do not include fake facts about a person that is looking for job. 
            I have introduced myself as: {aboutMe}.
            Please use only information about me that I have explicitly written.
            My name is {username}.
            The response should be a string where cover letters are separated by special character = #,
            do not include technical words as cover letter 1 or two, just pure text related to cover letter.
            Some tips for you:
            1. Introduce myself and Identify the Job for Which I'm Applying.
            2. Mention The Relevant Experience That Makes You a Good Candidate if there is any.
            3. Show Them I'm Enthusiastic and Excited About the Chance to Work With Them.
            4. Be Sincere and Direct.
            5. Don’t Waste Their Time With Irrelevant Sentences.
            
            Each cover letter intro should be tailored to that particular job, company, hiring manager, and situation.
            Here are the best and most effective examples:
            1. Start With an Accomplishment if any
            2. Inform the Company of What I Can Offer Them
            3. Show That I Love the Company
            4. Name-Drop by Saying You Know Someone Relevant
            5. Exude Enthusiasm, Excitement, and Passion
            6. Refer to Their Current Events
            7. Display Some Creativity & Humor
            8. Be Direct
            9. Craft a Powerful Belief Statement
            
            Structure cover letters with easy to read paragraphs.
            """
        )
        print("This is prompt: " + prompt.format(aboutMe=process.custom_msg, position=process.selected_position, username=username))
        chain = LLMChain(llm=llm, prompt=prompt)

        response = chain.run(aboutMe=process.custom_msg, position=process.selected_position, username=username)
        print(f"This is response {response}")
        return response.split("#")

    @classmethod
    def generate_positions(cls, customer_msg: str):
        prompt = PromptTemplate(
            input_variables=["aboutMe"],
            template="I have "
                     "introduced "
                     "myself as: {aboutMe}. "
                     "Please propose for me 5 names of positions that would be suitable for as comma separated string. "
                     "Make sure that positions are not similar to each other."
        )
        print("This is prompt from generate propositions " + prompt.format(aboutMe=customer_msg))
        chain = LLMChain(llm=llm, prompt=prompt)

        response = chain.run(aboutMe=customer_msg)
        return [s.strip() for s in response.split(",")]

    @classmethod
    def generate_interview_questions(cls, process: Process):
        prompt = PromptTemplate(
            input_variables=["coverLetter"],
            template="""Based on cover letter: {coverLetter}, please prepare 5 interview questions separated by 
            special character: #."""
        )
        print("This is prompt from generate propositions " + prompt.format(coverLetter=process.covered_letters[0]))
        chain = LLMChain(llm=llm, prompt=prompt)

        response = chain.run(coverLetter=process.covered_letters[0])
        print(f"This is response from generate_interview_questions questions {response}")
        return [s.strip() for s in response.split("#")]

    @classmethod
    def validate_interview_question_answer(cls, process: Process, question: str, answer: str):
        prompt = PromptTemplate(
            input_variables=["coverLetter", "question", "answer", "position"],
            template="""
             Based on the cover letter: {coverLetter}, that should help me to apply for position like {position},
             you have generated interview question: {question}.
             Here you are my answer: {answer}.
             Evaluate it, but don't be cruel. Remember that I do not have much experience.
             You can use sandwich method of evaluation.
             Do it in max 50 words.
             If I'm wrong propose valid answer.
            """
        )
        print("This is prompt from generate propositions " + prompt.format(coverLetter=process.covered_letters[0],
                                                                           position=process.selected_position,
                                                                           question=question,
                                                                           answer=answer))
        chain = LLMChain(llm=llm, prompt=prompt)

        response = chain.run(coverLetter=process.covered_letters[0], question=question, answer=answer,
                             position=process.selected_position)
        print(f"This is response from validate_interview_question_answer {response}")
        return response
