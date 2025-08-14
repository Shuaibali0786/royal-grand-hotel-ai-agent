# main.py
import os
import asyncio
import chainlit as cl
from agents import Runner, InputGuardrailTripwireTriggered, OutputGuardrailTripwireTriggered
from my_config.config import config
from my_agent.my_agents import hotel_agent  # Tumhara Gemini + Guardrails agent

# ---------------- CLI MODE ----------------
def run_cli():
    try:
        prompt = input(
            "🏨 Welcome to Royal Grand Hotel - Inspired by 5-Star Luxury.\n"
            "💬 Please enter your question about the hotel: "
        )
        res = Runner.run_sync(
            starting_agent=hotel_agent,
            input=prompt,
            run_config=config
        )
        print(res.final_output)

    except InputGuardrailTripwireTriggered as e:
        print(f"🚫 Trip input detected:\n{e}")

    except OutputGuardrailTripwireTriggered as e:
        print(f"🚫 Trip output detected:\n{e}")


# ---------------- CHAINLIT MODE ----------------
@cl.on_chat_start
async def start():
    """Show welcome message when chat starts"""
    await cl.Message(
        content="🏨 Welcome to Royal Grand Hotel - Your luxury stay awaits! 🛎️"
    ).send()


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
        await cl.Message(content=f"🚫 Input blocked: {e}").send()

    except OutputGuardrailTripwireTriggered as e:
        await cl.Message(content=f"🚫 Output blocked: {e}").send()


# ---------------- ENTRY POINT ----------------
if __name__ == "__main__":
    if os.environ.get("MODE", "CLI").upper() == "CLI":
        run_cli()
    else:
        asyncio.run(cl.main())
