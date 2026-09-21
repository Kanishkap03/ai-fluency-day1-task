from workflow import workflow
from agent import agent

QUESTION = "My income is Rs. 15,000 this month. How much will I have left after paying all my expenses?"

print("Q:", QUESTION)
print("\nWorkflow :", workflow(QUESTION))
print("\nAgent    :", agent(QUESTION))
