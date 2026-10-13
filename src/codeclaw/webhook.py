import json
from typing import Callable
from codeclaw.config import get_config

class WebhookNotificationDispatcher:
    def __init__(self):
        self.config = get_config()
        self.webhooks: dict[str, Callable] = {}

    def register webhook(self, endpoint: str, handler: Callable) -> None:
        