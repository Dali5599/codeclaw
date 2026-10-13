from codeclaw.parsers.markdown_call_parser import MarkdownCallParser
from codeclaw.parsers.json_call_parser import JsonCallParser
import typer

runner = CliRunner()

def parse_tool_calls(cmd):
    if cmd == 'markdown':
        parser = MarkdownCallParser() \n        return parser.parse(markdown_text)

def cli_app(ctx):
    global runner
    app_name = "Tool Call Parser"
def main():
def help(ctx):