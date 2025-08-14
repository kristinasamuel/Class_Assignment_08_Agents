# 1. Create Two Agents
# BotAgent: Handles FAQs, order lookup (function tools).
# HumanAgent: For escalation (handoff).
# Experiment with the effect of tool_choice and metadata in responses.

# Main Agent 
# BotAgent: Handles FAQs, order lookup (function tools).

from agents import Agent, ModelSettings , handoff
from my_config.config import model
from my_agents.human_agent import human_agent
from tools.tool import get_order_status ,is_enabled,error_function
from guardrials.guardrial import input_check_guardrial, output_check_guardrial

bot_agent = Agent(
    name = "Vivek oberoi",
    instructions= """ 
    You are a helpful customer support bot.  
    - First, check the user input for any negative, rude, harmful, or offensive language.  
    - If input is fine, handle FAQs about products politely.  
    - If the query is about an order:  
      - Call `is_enabled`.  
      - If `True`, call `get_order_status`.  
      - If order not found, call `error_function`.
    - If the query is complex,ask inventory,payment and store detail handoffs to the  HumanAgent
    - If the user asks for any of the above sensitive details, politely refuse to provide it.
    - Always respond positively, respectfully, and professionally.

    """,
    model= model,
    input_guardrails=[input_check_guardrial],
    handoffs = [handoff(human_agent)],
    tools=[get_order_status,is_enabled,error_function],
    output_guardrails= [output_check_guardrial],
)