from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv

load_dotenv()

def build_agent() :
    return Agent (
        model = Groq(id = ""),
        markdown = True, # gives output in proper format
        instructions ="you are helpful and expert travel agent.",
    )
agent = build_agent()

