# Overview

## Agents

- The goal of an Agent is to use an LLM and a prompt to **choose a sequence of actions to take.**
- They are designed to perform **well-defined tasks**, such as answering questions, summarizing text, translating languages, and doing math.    
  - Its **inputs** are:
     - Tools: Descriptions of available tools (read below)
     - User Input: The objective, at a high level
     - Intermediate steps: Any action + tool output pairs that were previously executed to produce the User Input
  - Its **output** is *one* of the following:
     - AgentAction: The next action to take
     - AgentFinish: The final response to send to the user
- With regular chains, a sequence of actions is hardcoded. With agents, an LLM is used to determine which actions to take, and in which order. 

## Tools

- Tools are functions that an agent can invoke. There are two important design considerations around tools:
    - Giving the agent access to the tools it needs
    - Describing the tools in a way that is most helpful to the agent

- Tools are critical in building a working agent.
    - If an agent doesn't have access to the right set of tools, it can't accomplish the objectives you give it.
    - If the tools aren't described well, the agent won't know how to use them.

# Setup

### Helpful Resources

[LangChain Documentation on Agents] (https://python.langchain.com/docs/modules/agents/)