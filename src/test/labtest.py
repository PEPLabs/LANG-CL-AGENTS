"""
This file will contain test cases for the automatic evaluation of your
solution in main/lab.py. You should not modify the code in this file. You should
also manually test your solution by running app.py.
"""

import os
import unittest

from langchain.chat_models import AzureChatOpenAI

from src.main.lab import agent_executor


class TestLLMResponse(unittest.TestCase):
    """
    This test will verify that the connection to an external LLM is made. If it does not
    work, this may be because the API key is invalid, or the service may be down.
    If that is the case, this lab may not be completable.
    """
    def test_llm_sanity_check(self):
        llm = AzureChatOpenAI(model_name="gpt-35-turbo")

    """
    This test will verify that the agent uses the appropriate tool for the task given.
    """
    def test_appropriate_tools_used_by_agent(self):

        response = agent_executor.invoke(
            {"input": "What is the length of the word Jurassic?"},
        )

        tool_used = response["intermediate_steps"][0][0].tool

        # Verifies that the get_word_tool is used when the agent is asked to find the length of a word
        self.assertEqual("get_word_length", tool_used)

        response = agent_executor.invoke(
            {"input": "What is 3 cubed?"},
        )

        tool_used = response["intermediate_steps"][0][0].tool

        # Verifies that the get_cube_of_number is used when the agent is asked to find the cube of a number
        self.assertEqual("get_cube_of_number", tool_used)

    """
    This test will verify that the agent produces the correct answer.
    """
    def test_agent_gets_correct_answer(self):

        response = agent_executor.invoke(
            {"input": "What is the length of the word Jurassic?"},
        )

        self.assertEqual(response["output"], "8")

        response = agent_executor.invoke(
            {"input": "what is 3 cubed?"},
        )

        self.assertEqual(response["output"], "27")

