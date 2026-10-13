"""
Core unit tests for CodeClaw.
"""
import pytest
from codeclaw import __version__
from codeclaw.config import get_config
from typer.testing import CliRunner
from codeclaw.cli import app

runner = CliRunner()

def test_version():
    assert __version__ == "0.1.0"

def test_config():
    cfg = get_config()
    assert cfg.app_name == "CodeClaw"
    assert cfg.version == "0.1.0"
    assert cfg.enable_sandbox is True

def test_cli_version():
    result = runner.invoke(app, ["version"])
    assert result.exit_code == 0
    assert "CodeClaw" in result.stdout

def test_cli_doctor():
    result = runner.invoke(app, ["doctor"])
    assert result.exit_code == 0
    assert "operational" in result.stdout
