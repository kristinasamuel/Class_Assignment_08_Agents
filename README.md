 ## 📌 Class Assignment Smart Customer Support Bot 🤖

## Objective
Create a customer support bot using OpenAI's Agent SDK that can handle basic FAQs, fetch order statuses, and escalate to a human agent when necessary. The bot should also implement guardrails to ensure positive interactions and showcase advanced features of the SDK.

- Answer basic FAQs  
- Fetch order status  
- Escalate to a human agent (handoffs)  
- Safe interactions with **input guardrails**

---

## 📚 Topics Covered

- Agent → Main brain of the bot, processes user queries
- Function Tool → Allows the bot to fetch order details from a simulated database
- Handoffs → Transfers chat to a human when bot can’t solve the problem
- Input Guardrails → Blocks rude or unsafe inputs before they reach the bot
---

## 🛠 Steps to Run

1. **Initialize Project**
   ```
   uv init .
   ```

2. **Install OpenAI Agents SDK**
   ```
   uv add openai-agents
   ```

3. **Run the Bot**
   ```
   uv run main.py
   ```