from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv
from agno.db.sqlite import SqliteDb

load_dotenv("../.env")

db = SqliteDb(db_file = "agno.db")
db.clear_memories()

def build_agent() :
    return Agent (
        db=db,
        model = Groq(id = "qwen/qwen3-32b"),
        markdown = True, # gives output in proper format
        add_history_to_context=True
    )
agent = build_agent()

agent.print_response("what is the capital of Australia ?")
agent.print_response("what is the best time to visit it?")
