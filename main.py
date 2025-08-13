# Main file to run the bot agent

from agents import Runner,trace 
from my_agents.bot_agent import bot_agent
import asyncio

async def main():
    try:
        with trace("Customer Support Bot Agent"):
            prompt = input(" \n Enter your question: ")
            result = await Runner.run(bot_agent, prompt)
            print("\n==========> AGENT OUTPUT <==========")
            print(result.final_output)
    except Exception as ex:
        print("🚨Tripwire triggered. Guardrail activated:", ex)

asyncio.run(main())