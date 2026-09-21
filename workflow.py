import re
from config import EXPENSES, QUESTIONS

def workflow(question):
    text = question.lower()

    # Step 1: find which expense names are mentioned (whole words only)
    names = [name for name in EXPENSES if re.search(rf"\b{name.lower()}\b", text)]
    amounts = [EXPENSES[name] for name in names]

    # Rule 1: no known expense name -> nothing we can do
    if not amounts:
        return "Sorry, I can only answer questions about my expenses."

    # Rule 2: "cut ... N%" -> total of the named expenses after the cut
    percent = re.search(r"(\d+)\s*%", text)
    if "cut" in text and percent:
        total = sum(amounts) * (1 - int(percent.group(1)) / 100)
        return f"After a {percent.group(1)}% cut, {' + '.join(names)} = Rs. {total:,.0f}"

    # Rule 3: exactly one expense named -> just look it up
    if len(amounts) == 1:
        return f"{names[0]} expense: Rs. {amounts[0]:,}"

    return "Sorry, I do not have a rule for this type of question."

if __name__ == "__main__":
    print("\n=== SYSTEM 2: RULE-BASED WORKFLOW (no LLM) ===\n")
    for question in QUESTIONS:
        print("Q:", question)
        print("A:", workflow(question))
        print("-" * 70)
