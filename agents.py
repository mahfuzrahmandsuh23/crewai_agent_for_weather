# agents.py
import os
from dotenv import load_dotenv
from crewai import Agent,LLM
from langchain_groq import ChatGroq
from tools import search_tool, file_reader, citation_formatter

# Load API key from .env
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Define Groq LLM
llm = LLM(
    model="gpt-4",
    temperature=0.7,
    base_url="https://api.openai.com/v1",
    api_key=openai_api_key
)

research_agent = Agent(
    role="Researcher",
    goal="Find and summarise relevant academic sources.",
    backstory="An academic assistant with access to scientific search tools, trained to extract reliable research summaries.",
    tools=[search_tool, file_reader],
    llm=llm,
    verbose=True # ADD THIS
)

outliner_agent = Agent(
    role="Outliner",
    goal="Create a structured academic outline based on the research.",
    backstory="An experienced academic editor, skilled in organising research papers for clarity and logical flow.",
    llm=llm,
    verbose=True # ADD THIS
)

writer_agent = Agent(
    role="Writer",
    goal="Draft academic paper sections from outline and research.",
    backstory="A scientific writer focused on turning research and outlines into publishable academic prose.",
    llm=llm,
    verbose=True # ADD THIS
)

reviewer_agent = Agent(
    role="Reviewer",
    goal="Edit the draft for clarity, correctness, and format citations.",
    backstory="A senior editor with knowledge of APA style and strong attention to grammar and coherence.",
    tools=[citation_formatter],
    llm=llm,
    verbose=True # ADD THIS
)