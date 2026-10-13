import asyncio
from typing import Dict, Any

class ReactAgent:
    def __init__(self):
        self.state_queue: asyncio.Queue = asyncio.Queue()
        self.transition_map: Dict[Any, Any] = {}

    async def step(self) -> None:
        while not self.state_queue.empty():
            current_state = await self.state_queue.get()
            action = self.get_action(current_state)
            next_state, reward, done = self.transition(current_state, action)

            await self.state_queue.put((next_state, reward, done))

    async def run(self):
        for step in itertools.count():
            await self.step()

        while not self.state_queue.empty():
            current_state, _, _ = await self.state_queue.get()