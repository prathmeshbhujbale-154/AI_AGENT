from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv

load_dotenv("../.env")

def build_agent() :
    return Agent (
        model = Groq(id = "llama-3.3-70b-versatile"),
        markdown = True, # gives output in proper format
        instructions ="you are helpful and expert travel agent.",
        add_datetime_to_context=True
    )
agent = build_agent()

agent.print_response("my budget is 1L INR , should i travel to goa or phuket")
