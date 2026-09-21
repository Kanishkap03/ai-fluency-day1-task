# Day 1 Task — Chatbot vs Rule-Based Workflow vs AI Agent

## Personal Expense Management Scenario

This project demonstrates the difference between a **Plain Chatbot**, a **Rule-Based Workflow**, and an **AI Agent** using a private personal-expense scenario.

The goal is to solve the same money-related problems using three different approaches and compare them based on flexibility, decision-making, tool usage, private-data access, multi-step task handling, automation, and reliability.

---

## Scenario

The private data represents monthly expenses stored inside the application:

| Category      | Amount |
| ------------- | -----: |
| Rent          | ₹6,000 |
| Food          | ₹3,500 |
| Transport     | ₹1,200 |
| Internet      |   ₹600 |
| Entertainment | ₹1,500 |

The data is private application data and is not provided to the plain chatbot.

### Total Monthly Expenses

₹6,000 + ₹3,500 + ₹1,200 + ₹600 + ₹1,500 = **₹12,800**

---

## Test Questions

The three systems are tested using the same four questions:

### Question 1

**How much did I spend on Food this month?**

Correct answer: **₹3,500**

### Question 2

**What will I spend on Food and Transport together if I cut both by 10%?**

Calculation:

* Food = ₹3,500
* Transport = ₹1,200
* Total = ₹4,700
* After 10% reduction = ₹4,230

Correct answer: **₹4,230**

### Question 3

**Is Rent more than Food, and by how much?**

Calculation:

₹6,000 − ₹3,500 = **₹2,500**

Correct answer: **Yes, Rent is ₹2,500 more than Food.**

### Question 4

**Write a two-line motivational message about saving money.**

This question does not require access to the private expense data.

---

## Systems Compared

### 1. Plain Chatbot

The plain chatbot uses an LLM alone.

It does not have access to the private expense dictionary and does not have any tools or predefined rules for retrieving the expenses.

Therefore, for questions that require private expense information, the chatbot may either say that it does not have access to the data or generate unsupported numbers.

For a general-language question such as the motivational message, it can respond normally because no private data is required.

---

### 2. Rule-Based Workflow

The rule-based workflow does **not use an LLM**.

It uses predefined Python conditions and rules to identify expense categories and perform specific calculations.

For the implemented scenario, it can correctly handle:

* A direct expense lookup.
* A combined expense calculation with a percentage reduction.

However, it cannot automatically handle a new type of question unless a corresponding rule has been programmed.

For example, the comparison question about Rent and Food is rejected because no rule was created for that type of question.

The workflow is therefore predictable but rigid.

---

### 3. AI Agent

The AI Agent combines:

**LLM + Tools + Loop**

The agent has access to two tools:

* `get_expense` — retrieves an expense from the private data.
* `calculator` — performs arithmetic calculations.

The agent follows a repeated process:

1. **Reason** about what the user is asking.
2. **Act** by selecting and calling the required tool.
3. **Observe** the returned result.
4. Continue the loop if another action is required.
5. Return the final answer when the task is complete.

The agent has a maximum step limit to prevent an endless tool-calling loop.

---

## Comparison

| Basis for comparison     | Plain Chatbot                                             | Rule-Based Workflow                           | AI Agent                                            |
| ------------------------ | --------------------------------------------------------- | --------------------------------------------- | --------------------------------------------------- |
| Flexibility              | High for general language, but cannot access private data | Limited to programmed rules                   | Can handle new requests using available tools       |
| Decision-making          | Generates a response from the prompt                      | Programmer-defined conditions decide the path | LLM decides which tools/actions are required        |
| Tool usage               | None                                                      | None                                          | Uses expense lookup and calculator                  |
| Private-data access      | Cannot access the expense dictionary                      | Can access data through hard-coded rules      | Accesses data through tools                         |
| Multi-step task handling | Cannot reliably perform private-data tasks                | Handles only predefined multi-step cases      | Can retrieve data, calculate, compare, and continue |
| Automation               | Generates text only                                       | Automatically executes predefined steps       | Can automatically perform multiple tool actions     |
| Reliability              | Can lack data or invent numbers                           | Predictable for supported rules               | Grounded by tool results but model-dependent        |

---

## Challenge

### Question

> My income is ₹15,000 this month. How much will I have left after paying all my expenses?

The rule-based workflow does not have a rule for this open-ended question and returns:

```text
Workflow : Sorry, I can only answer questions about my expenses.
```

The AI Agent can approach the problem by retrieving the five expense categories and calculating the total.

The calculation is:

```text
Rent          = ₹6,000
Food          = ₹3,500
Transport     = ₹1,200
Internet      = ₹600
Entertainment = ₹1,500
--------------------------------
Total         = ₹12,800

Income        = ₹15,000
Expenses      = ₹12,800
--------------------------------
Remaining     = ₹2,200
```

Expected answer:

**₹2,200 remaining.**

This challenge demonstrates the difference between a fixed workflow and an agent that can perform multiple tool calls and calculations for a question that was not explicitly implemented as a rule.

---

## Key Observations

The plain chatbot can understand natural language and generate responses, but it does not automatically have access to the private expense data. This makes it unsuitable for answering private-data questions unless the required information is explicitly provided.

The rule-based workflow is predictable because its behavior is determined by predefined conditions. It correctly handles the questions for which rules were written, but it fails when the question falls outside those rules. Even a rephrased question can fail if it no longer matches the expected pattern.

The AI Agent is more flexible because the LLM can determine which tools are required. For example, the comparison between Rent and Food requires two expense lookups followed by a calculation. The agent can perform these actions through its tool-calling loop rather than requiring a separate hard-coded rule for that exact question.

---

## Model Used

**Provider:** Groq

**Model:** `openai/gpt-oss-20b`

The same model is used for the LLM-based chatbot and agent components.

The rule-based workflow does not use an LLM.

---

## Learning Outcome

This experiment demonstrates the practical distinction between the three approaches.

A **plain chatbot** is primarily an LLM that generates responses from the conversation. A **rule-based workflow** follows predefined conditions and does not require an LLM. An **AI Agent** combines an LLM with tools and a loop, allowing it to decide what actions are needed, use the available tools, observe their results, and continue until the task is completed.

The money-management scenario shows why the three approaches behave differently even when they receive the same user questions.

---

## Conclusion

A plain chatbot is suitable when the task mainly requires natural-language understanding or generation and does not depend on private application data.

A rule-based workflow is suitable when the possible inputs and required actions are known in advance and predictable behavior is important. Examples include fixed form validation, predefined calculations, and deterministic business rules.

An AI Agent is suitable when a task requires multiple actions, access to external or private data through tools, calculations, or decisions about what to do next. Examples include personal-data assistants, research workflows, scheduling tasks, and multi-step data analysis.

The experiment shows that an agent is not simply a more advanced chatbot. Its defining feature is the combination of **LLM + Tools + Loop**, allowing it to act on a task rather than only generate a response.
