{
import os
from typing import Dict, List

class WebTerminal:
    def __init__(self):
        self.ansi_escapes = {{
            [30m": "Reset",\n            [31m": "Red",\n            [32m": "Green",\n            [33m": "Yellow",\n            [34m": "Blue",\n            ¡B[35m": "Magenta",\xa1B[36m": "Cyan",\xa1B[37m": "White-Background Black Text",\n        }
        self.log_lines: List[str] = []
        
    def listen_stream(self, stream):
        for line in stream:
            ansi_escape_sequence = None
            for key, value in self.ansi_escapes.items():\n                if f"\x1B[{key}m" == line.rstrip()[:6]:\n                    ansi_escape_sequence = value
\n            logged_message = f "{line.strip()} {ansi_escape_sequence}" if ansi_escape_sequence else line.strip()
\n            print(logged_message, end="")

    def get_log_lines(self):
        return self.log_lines

    def add_line(self, line):
        self.log_lines.append(line)