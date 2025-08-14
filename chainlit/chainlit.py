import chainlit as cl
from agents import Runner, InputGuardrailTripwireTriggered, OutputGuardrailTripwireTriggered
from my_config.config import config
from my_agent.my_agents import hotel_agent

@cl.on_chat_start
async def start():
    await cl.Message(content="👋 Welcome to Royal Grand Hotel Assistant! Please ask me anything about the hotel.").send()

@cl.on_message
async def main(message: cl.Message):
    try:
        res = await Runner.run(
            starting_agent=hotel_agent,
            input=message.content,
            run_config=config
        )
        await cl.Message(content=res.final_output).send()

    except InputGuardrailTripwireTriggered as e:
        await cl.Message(content=f"⚠️ Your question was not related to Royal Grand Hotel.\n{e}").send()

    except OutputGuardrailTripwireTriggered as e:
        await cl.Message(content=f"⚠️ My response contained disallowed content.\n{e}").send()
