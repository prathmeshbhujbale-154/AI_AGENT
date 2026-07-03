from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv
from agno.tools.duckduckgo import DuckDuckGoTools

load_dotenv("../.env")

def build_agent() :
    return Agent (
        model = Groq(id = "qwen/qwen3-32b"),
        tools=[DuckDuckGoTools()],
        markdown = True, # gives output in proper format
        instructions ="you are helpful and expert travel agent.",
        add_datetime_to_context=True
    )
agent = build_agent()

agent.print_response("my budget is 1L INR , should i travel to goa or phuket")
