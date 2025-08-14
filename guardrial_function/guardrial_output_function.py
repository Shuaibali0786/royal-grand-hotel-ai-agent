from agents import GuardrailFunctionOutput, output_guardrail, RunContextWrapper, Runner
from my_config.config import config
from my_agent.guardrials_agents import output_guardrail_agent

@output_guardrail
async def guardrial_output_function(ctx: RunContextWrapper, agent, output):
    result = await Runner.run(
        starting_agent=output_guardrail_agent,
        input=output,
        context=ctx.context,
        run_config=config
    )
    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=not result.final_output.is_hotel_sannata_query
    )
