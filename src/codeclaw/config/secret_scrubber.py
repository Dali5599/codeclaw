import os
from config import get_config

class SecretScrubber:
    def __init__(self, config):
        self.config = config
        self.scrubbed_env_vars = []

    def add_sensible_var(self, var_name, value):
        if not self.scrubbed_env_vars:
            raise ValueError("No secret scrubber instance created. Create one using `SecretScrubber(config)`")
        os.environ[var_name] = f