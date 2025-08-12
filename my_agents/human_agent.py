# HumanAgent: For escalation (handoff).
#  Agent Handoff
# If the bot detects a query it can’t handle or sentiment is negative, handoff to the HumanAgent.

from agents import Agent
from my_config.config import model

# Human Agent  
human_agent = Agent(
    name = "Human Agent",
    instructions= """
    You are a human customer support agent.
     - Handle escalated queries from the BotAgent.
     - Provide detailed and clear responses to user queries.
     """,
     model = model
)

