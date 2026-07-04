from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools

load_dotenv("../.env")

def build_agent() :
    return Agent (
        model = Groq(id = "qwen/qwen3-32b"),
        tools=[DuckDuckGoTools(), YFinanceTools()],
        markdown = True, # gives output in proper format
        instructions ="you are helpful and expert travel agent.",
        add_datetime_to_context=True,
        description="You are a comprehensive investment analyst with access to all financial data functions.",
        instructions=[
            "Use any financial function as needed for investment analysis",
            "Format your response using markdown and use tables to display data",
            "Provide detailed analysis and insights based on the data",
            "Include relevant financial metrics and recommendations"
        ],
    )
agent = build_agent()

agent.print_response("my budget is 1L INR , should i travel to goa or phuket")
