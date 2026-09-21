"""System 3: an AI agent. LLM + tools + loop."""

import json

from config import client, MODEL, QUESTIONS, banner
from tools import TOOLS, TOOL_FUNCTIONS


SYSTEM_PROMPT = (
    "You are a personal budget assistant. "
    "Never guess an expense: always use get_expense. "
    "Use calculator for any arithmetic. "
    "Available categories: Rent, Food, Transport, Internet, Entertainment. "
    "If no tool is needed, answer directly."
)


def agent(question, max_steps=8, verbose=True):
    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": question
        }
    ]

    for step in range(1, max_steps + 1):

        # 1. REASON:
        # Ask the LLM what to do next.
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            tools=TOOLS,
            temperature=0
        )

        message = response.choices[0].message

        # 2. If no tool is requested, the LLM has finished.
        if not message.tool_calls:
            return message.content.strip()

        # Preserve the complete assistant message exactly as returned
        # by the model. This is important for GPT-OSS tool calling.
        messages.append(
            message.model_dump(exclude_none=True)
        )

        # 3. ACT and OBSERVE:
        # Execute the requested tools and send their results
        # back to the LLM.
        for call in message.tool_calls:

            name = call.function.name

            arguments = json.loads(
                call.function.arguments or "{}"
            )

            function = TOOL_FUNCTIONS.get(name)

            if function:
                result = function(**arguments)
            else:
                result = f"Unknown tool: {name}"

            if verbose:
                print(
                    f"   step {step}: "
                    f"{name}({arguments}) -> {result}"
                )

            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": call.id,
                    "name": name,
                    "content": result
                }
            )

    return "Stopped: maximum steps reached without a final answer."


if __name__ == "__main__":

    banner("SYSTEM 3: AI AGENT")

    for question in QUESTIONS:

        print("Q:", question)

        print("A:", agent(question))

        print("-" * 70)