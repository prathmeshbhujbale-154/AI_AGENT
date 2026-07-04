from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv
from agno.team import Team

load_dotenv("../.env")

eng_agent = Agent(name="English Agent" , role="you answer questions in english")
frc_agent = Agent(name="french Agent" , role="you answer questions in french")
hin_agent = Agent(name="hindi Agent" , role="you answer questions in hindi")

team_leader = Team(
    name = "answer and translation team",
    members = [eng_agent, frc_agent, hin_agent],
    model = Groq(id = "qwen/qwen3-32b"),
    markdown=True,
    show_members_responses=True,
    instructions="""all agents must response to answer the query in their specific language.
                    do not route just one agent.
                    output the response of all agents.
                """
)

team_leader.print_response("who is prime minister  of india")