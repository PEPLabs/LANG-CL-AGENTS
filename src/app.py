import io
import sys
import time

from langchain_core.agents import AgentAction

from main.lab import agent_executor

"""
This file will contain some sample code that invokes the agent with two different tasks.
If the lab is completed correctly, the console should show the agent determining which tool to use for the job. 
You may modify this file in any way, it will not affect the test results.
NOTE: The agent will occasionally trip over itself and not pick the appropriate tool. 
Either be more descriptive in your tools descriptions, or just run app.py again if it worked previously.
"""


def main():

    print("Using the agent to find the length of a word:")
    agent_executor.invoke(
        {"input": "What is the length of the word boogaloo?"},
    )

    print("Using the agent to find the cube of a number:")
    agent_executor.invoke(
        {"input": "What is 7 cubed?"}
    )

    print("+++++++++++++++")

    response = agent_executor.invoke(
        {"input": "What is the length of the word boogaloo?"},
    )

    print(response["output"])


if __name__ == '__main__':
    main()