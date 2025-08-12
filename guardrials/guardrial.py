# 3.Guardrails
# Use @input guardrail to check for offensive or negative language. If detected, return a warning or rephrase the response.

from agents import Agent, Runner,input_guardrail,GuardrailFunctionOutput
from my_config.config import model
from schema.schema import IsNegativePrompt

# Guardrial Agent
guardrial_agent = Agent(
    name="Guardrial Agent",
    instructions="""
       check the input prompt in bot agent for negative or offensive language.
    """,
    model = model,
    output_type=IsNegativePrompt,
)

# Input Guardrail Function
@input_guardrail
async def input_check_guardrial(ctx, agent: Agent, input: str) -> GuardrailFunctionOutput:
    result = await Runner.run(guardrial_agent, input, context=ctx)
    print("🛡️ Guardrial Agent Decision:")
    print(result.final_output)

    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered= result.final_output.IsNegativePrompt
    )