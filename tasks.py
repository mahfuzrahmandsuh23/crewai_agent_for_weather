from crewai import Task
from agents import research_agent, outliner_agent, writer_agent, reviewer_agent

task1 = Task(
    agent=research_agent,
    description="Research and summarise academic papers on 'AI in Climate Change Forecasting'.",
    expected_output="A list of at least 3 well-summarised academic papers with relevance to the topic."
)

task2 = Task(
    agent=outliner_agent,
    description="Create a detailed outline for a research paper based on those summaries.",
    expected_output="A clear and logical outline with standard academic sections (e.g., Introduction, Method, etc.)"
)

task3 = Task(
    agent=writer_agent,
    description="Write the draft of the paper using the outline and research findings.",
    expected_output="A polished academic draft, minimum 500 words, using the provided outline."
)

task4 = Task(
    agent=reviewer_agent,
    description="Review the draft and apply citation formatting using APA style.",
    expected_output="An improved draft with clear grammar, better structure, and correctly formatted citations."
)

all_tasks = [task1, task2, task3, task4]
