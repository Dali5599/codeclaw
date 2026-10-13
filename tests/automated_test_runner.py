import pytest
import unittest
import pkg_resources
from codeclaw.cli import app
from typer.testing import CliRunner

def get_cli_runner(name):
    cli = app
    runner = CliRunner()
    return runner.invoke(cli, [name])

class AutomatedTestRunnerDetector:
    def __init__(self):
        self.pytest = None
        self.jest = None
        self.cargo = None
        self.go = None

    def detect_pytest(self):
        if not hasattr(sys,