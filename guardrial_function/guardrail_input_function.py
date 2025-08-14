import asyncio
from agents import (
    Agent,
    input_guardrail,
    RunContextWrapper,
    TResponseInputItem,
    GuardrailFunctionOutput,
    Runner
)
from my_config.config import config
from my_agent.guardrials_agents import input_guardrail_agent

@input_guardrail
async def input_guardrail_fn(
    ctx: RunContextWrapper,
    agent: Agent,
    input: str | list[TResponseInputItem]
) -> GuardrailFunctionOutput:
    print("Working on it...")

    result = await Runner.run(
        starting_agent=input_guardrail_agent,
        input=input,
        context=ctx.context,
        run_config=config
    )
    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=not result.final_output.is_hotel_sannata_query
    )
