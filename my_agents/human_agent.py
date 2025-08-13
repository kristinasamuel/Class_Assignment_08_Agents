# HumanAgent: For escalation (handoff).
#  Agent Handoff
# If the bot detects a query it can’t handle or sentiment is negative, handoff to the HumanAgent.

from agents import Agent
from my_config.config import model

# Human Agent  
human_agent = Agent(
    name = "Human Agent",
    instructions= """
        You are a friendly and knowledgeable human customer support agent.
            - Provide detailed, accurate, and helpful answers for complex questions.
            - If the query involves inventory, store details, or payment details, give complete and clear information.
            - Respond politely and professionally, ensuring the customer feels valued.    
         """,
     model = model,
)

