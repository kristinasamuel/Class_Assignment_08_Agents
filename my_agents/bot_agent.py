# 1. Create Two Agents
# BotAgent: Handles FAQs, order lookup (function tools).
# HumanAgent: For escalation (handoff).
# Experiment with the effect of tool_choice and metadata in responses.

# Main Agent 
# BotAgent: Handles FAQs, order lookup (function tools).

from agents import Agent
from my_config.config import model
from my_agents.human_agent import human_agent
from tools.tool import get_order_status ,is_enabled,error_function
from guardrials.guardrial import input_check_guardrial
from openai import ModelSettings

bot_agent = Agent(
    name = "Vivek oberoi",
    instructions= """ 
    you are a helpfull customer support bot.
    - Answer user FAQs about products clearly and politely.
      - If the query is about an order, first call `is_enabled`.
      - If `is_enabled` returns True, then call `get_order_status`.
      - If `get_order_status` does not find the order, call `error_function`.
    - If the query is complex or the sentiment , hand off the conversation to the HumanAgent for further assistance.
    - Analyze the user input and determine if it contains any negative, rude, harmful, or offensive language.
    - Always maintain a positive, respectful, and professional tone.
    """,
    model= model,
    tools=[get_order_status,is_enabled,error_function],
    handoffs= [human_agent],
    input_guardrails=[input_check_guardrial],
    model_settings= ModelSettings(
        tool_choice = "auto",
        metadata = {
             "project": "Customer Support Bot",
        }
    )
)
