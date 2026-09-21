Day 1 Analysis — Chatbot vs Workflow vs AI Agent

1. Objective

To compare a plain chatbot, a rule-based workflow, and an AI agent using the same fictional expense data and test questions.

**Provider:** Groq
**Model:** `openai/gpt-oss-20b`

---

2. Comparison

| Question                       | Chatbot                          | Workflow          | Agent                                           |
| ------------------------------ | -------------------------------- | ----------------- | ----------------------------------------------- |
| Food expense                   | Could not access private data    | ₹3,500            | Retrieved Food using tool → ₹3,500              |
| Food + Transport after 10% cut | Could not calculate without data | ₹4,230            | Retrieved both + calculator → ₹4,230            |
| Rent vs Food                   | Could not access data            | No rule available | Retrieved both + calculator → ₹2,500 difference |
| Saving-money message           | Generated message                | No rule available | Generated message                               |
| Income ₹15,000 − all expenses  | Not recorded                     | No rule available | Calculated total ₹12,800 → ₹2,200 left          |

---

3. Reflection

Plain Chatbot

The chatbot could answer general-language questions, but it could not access the private expense data because no private-data tool was provided.

Rule-Based Workflow

The workflow was predictable because it followed predefined Python rules. It could answer questions for which rules were explicitly created, but it failed when no matching rule existed.

AI Agent

The agent consists of:

* **LLM:** Groq `openai/gpt-oss-20b`
* **Tools:** `get_expense` and `calculator`
* **Loop:** Allows multiple tool calls before producing the final answer.

For example, the challenge question required the agent to retrieve five expenses, calculate the total, and subtract it from the income.

Calculator Tool

The calculator provides reliable arithmetic instead of depending entirely on the LLM for calculations.

Workflow vs Agent

A fixed workflow is suitable for predictable, predefined tasks. An agent can handle more open-ended questions because it can decide which tools and steps are required.

Privacy

The experiment used Groq, a cloud-based LLM provider. With a local Ollama setup, model processing can be performed locally. Sensitive data should therefore be considered carefully when choosing between cloud and local models.

---

4. Conclusion

The experiment shows that a chatbot mainly generates language, a workflow follows fixed rules, and an agent combines an LLM, tools, and a loop to perform multiple steps and handle questions that were not explicitly hard-coded.
