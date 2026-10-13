
import json
class BudgetManager:
        def __init__(self, context_window):
            self.context_window = context_window
            self.budget_map = {}
        def truncate_prompt(self, prompt, max_chars=1000):
            if len(prompt) <= max_chars:
                return prompt
            max_length_in_context = int((len(prompt))) * self.context_window
truncated_prompt = prompt[:max_length_in_context]
remaining_chars = max_chars - max_length_in_context
for i, char in enumerate(truncated_prompt)[ 1 ]:
                    if len(char) <= remaining_chars:
                        break
                    else:
                        remaining_chars -= len(char) +  1
return truncated_prompt[:i] + '.\ '* (remaining_chars // 5)
    def set_budget(self, context_window_size):
            self.context_window = context_window_size
def encodeBudgetManager(budget_manager):
    return {\        'class' :   'CodeClaw.Budget'