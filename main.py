# main.py
from crew import build_crew
import os
from dotenv import load_dotenv

def main():
    load_dotenv()
    crew = build_crew()
    result = crew.kickoff()
    print("\n=== FINAL OUTPUT ===\n")
    print(result.raw)

if __name__ == "__main__":
    main()
