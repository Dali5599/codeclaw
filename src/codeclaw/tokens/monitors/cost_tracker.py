#Créer une classe de monitor qui suit la consommation du token et la gestion des dépenses.
from src.codeclaw.tokens import TokenUsageMonitor, DictAnyAny
class CostTracker(TokenUsageMonitor):
    def __init__(self):
        self.token_usage = {}

    async def start(self) -> None:
        pass
    def get_token_usage(self) -> Dict[Any, int]:
        return self.token_usage
    async def stop(self) -> None:
         # reset token usage
        self.token_usage = {}