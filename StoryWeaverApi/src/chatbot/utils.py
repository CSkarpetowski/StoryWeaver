from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent


@tool
def search_for_topic():
    pass


@tool
def search_for_reaction():
    pass


@tool
def what_to_do_with_location():
    pass


@tool
def what_to_do_with_enemies():
    pass


@tool
def what_to_do_with_talking():
    pass
