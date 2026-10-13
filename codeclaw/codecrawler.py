
import os
from colorama import Fore, Style
import markdown
from codeblock import CodeBlock

class Renderer:
    def __init__(self):
        self.builtins = {
            'h1': f'{Fore.BLUE}<h1>{end}{Style.RESET_ALL}'