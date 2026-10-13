"""
Configuration loader and settings for CodeClaw.
"""
import os
from pydantic import BaseModel, Field

class CodeClawConfig(BaseModel):
    app_name: str = "CodeClaw"
    version: str = "0.1.0"
    default_model: str = "claude-3-5-sonnet"
    workspace_dir: str = Field(default_factory=lambda: os.getcwd())
    max_tokens: int = 4096
    temperature: float = 0.2
    enable_sandbox: bool = True
    timeout_seconds: int = 60

def get_config() -> CodeClawConfig:
    return CodeClawConfig()
