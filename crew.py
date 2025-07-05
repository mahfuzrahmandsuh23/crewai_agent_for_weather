# crew.py
from crewai import Crew, Process
from tasks import all_tasks

def build_crew():
    return Crew(
        tasks=all_tasks,
        process=Process.sequential,  # Can be switched to .parallel
        verbose=True
    )
