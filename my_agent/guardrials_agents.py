from agents import Agent
from my_config.config import config
from data_schema.my_data_output import MyDataOutPut
from agents import Agent
from data_schema.my_data_output import MyDataOutPut

input_guardrail_agent = Agent(
    name="Input Guardrail Agent",
    instructions="Check if the given question is related to Royal Grand Hotel.",
    output_type=MyDataOutPut
)

output_guardrail_agent = Agent(
    name="Output Guardrail Agent",
    instructions="Check if the given hotel assistant's answer is only about Royal Grand Hotel and contains no unrelated or disallowed content.",
    output_type=MyDataOutPut
)