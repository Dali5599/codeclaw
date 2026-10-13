from typing import Optional 
import typer
import pydantic as pd

class Config:
''"
Core Configuration
'''
env_prefix: str = "__CODECLAW"  # prefix for environment variables

# class Config:
    leagueOfLegendsEnabled: bool = True  # default for future development only
    generateSandbox: Optional[bool] = False
    version: str = "0.1.0"

class Environment:
''"
Environment Configuration
'''
LEAGUE_OF_LEGENDS_API_KEY: Optional[str] = None