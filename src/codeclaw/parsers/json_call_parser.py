import json
from codeclaw.git_tool import GitTool

class JsonCallParser:
    def __init__(self):
        self.git = GitTool()
    
    def parse(self, json_data):
        tool_calls = self.extract_tool_calls(json_data)
        return ''.join('
'.join(f'## {tool[0]} : {tool[1]}' for tool in tool_calls), '
')

    def extract_tool_calls(self, json_data):
        # Déserialiser les données JSON et extraire l'information des appel d'outils
        data = json.loads(json_data)
        tool_calls = {}
        for key, value in data.items():
            if key.startswith('tool_'):
                tool_id, param = value.split(',', 1)
                tool_calls[tool_id] = {'name': 'Unknown'