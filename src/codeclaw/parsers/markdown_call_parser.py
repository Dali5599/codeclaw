import json
from markdown import MarkDown
from codeclaw.git_tool import GitTool

class MarkdownCallParser:
    def __init__(self):
        self.git = GitTool()
    
    def parse(self, markdown_text):
        # Extrair les appellations des outils avec leurs paramètres
        tool_calls = self.detect_tool_calls(markdown_text)
        return json.dumps(tool calls, indent=4)

    def detect_tool_calls(self, markdown_text):
        md = MarkDown(markdown_text)
        parsed_markdown = [line.strip() for line in md.output]
        # Recherche des mots-clés indiquant les outils et leurs paramètres
        tools_with_params = self.find_tools_with_params(parsed_markdown)
        return tools_with_params
    
    def find_tools_with_params(self, parsed_markdown):
        tool_calls = []
        for line in parsed_markdown:
            if ':' in line:
                tool_name, param = line.split(':', 1)
                tool_calls.append((tool_name.strip(), param.strip()))
        return tool_calls