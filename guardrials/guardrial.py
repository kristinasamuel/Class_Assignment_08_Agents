# 3.Guardrails
# Use @input guardrail to check for offensive or negative language. If detected, return a warning or rephrase the response.

from agents import Agent, Runner,input_guardrail,GuardrailFunctionOutput , output_guardrail
from my_config.config import model
from schema.schema import IsSensitiveOutput

# Guardrial Agent
guardrial_agent = Agent(
    name="Guardrial Agent",
    instructions="""
      - check the input prompt in bot agent for negative or offensive language.
      - also check the output of bot agent for sensitive or restricted information.
    """,
    model = model,
    output_type=IsSensitiveOutput,
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


# output guardrials 
@output_guardrail
async def output_check_guardrial(ctx, agent: Agent, output: IsSensitiveOutput) -> GuardrailFunctionOutput:
    text = output.response if hasattr(output, "response") else str(output)
    result = await Runner.run(guardrial_agent, text , context=ctx)
    print("🛡️ Output Guardrail Decision:")
    print(result.final_output)

    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=result.final_output.isRestrictedInfo
    )