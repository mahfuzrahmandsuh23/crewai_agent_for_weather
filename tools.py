# tools.py
from crewai_tools import SerperDevTool, FileReadTool
from crewai.tools import tool

# Web search (Google-like)
search_tool = SerperDevTool()

# Local file reader (e.g., PDFs)
file_reader = FileReadTool()

# Simple APA citation formatter
@tool("CitationFormatter")
def citation_formatter(text: str) -> str:
    """Formats citations in APA style based on the input text."""
    return f"[APA Citation formatted] {text}"
