
import os

def setup():
    from colorama import init, Color
    init()
    os.system('cls || clear')

class Theme:
    def __init__(self):
        self.colors = {
            'red': '#ff0000'