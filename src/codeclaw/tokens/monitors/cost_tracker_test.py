#Utiliser les tests Python pour vérifier si le code fonctionne correctement
import asyncio
from unittest.mock import Mock
from src.codeclaw.tokens import CostTracker
from src.codeclaw.SessionManage import ReactAgent
class TestCostTracker:
    def test__init__(self):
        cost_tracker = CostTracker()
        assert cost_tracker.token_usage == {}
...