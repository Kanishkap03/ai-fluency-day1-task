from config import client, MODEL, QUESTIONS, banner


SYSTEM_PROMPT = (
    "You are a helpful personal finance assistant. "
    "You do not have access to the user's private expense records or external tools. "
    "Do not invent or guess financial data. "
    "If a question requires private expense data that has not been provided "
    "in the conversation, clearly say that you cannot determine the answer."
)


def chatbot(question):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": question
            },
        ],
        temperature=0,
    )

    content = response.choices[0].message.content

    if content and content.strip():
        return content.strip()

    return (
        "I cannot determine the answer because I do not have access "
        "to your private expense data."
    )


if __name__ == "__main__":
    banner("SYSTEM 1: CHATBOT")

    for question in QUESTIONS:
        print("Q:", question)
        print("A:", chatbot(question))
        print("-" * 70)