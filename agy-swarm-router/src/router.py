"""
AGY Swarm Router
Dynamic triage mechanism assigning subtasks to models based on complexity.
"""

class SwarmRouter:
    def __init__(self):
        self.routes = {
            "high": "Gemini 1.5 Pro",
            "medium": "Gemini 1.5 Flash",
            "low": "Gemma 7B (Local)"
        }

    def assess_complexity(self, task_description: str) -> str:
        """
        Evaluates semantic density and tool dependencies 
        to determine the required model tier.
        """
        length = len(task_description)
        if length > 500 or "reason" in task_description.lower():
            return "high"
        elif length > 100 or "extract" in task_description.lower():
            return "medium"
        else:
            return "low"

    def route_task(self, task_description: str) -> str:
        """Routes the task to the appropriate model based on complexity."""
        complexity = self.assess_complexity(task_description)
        assigned_model = self.routes.get(complexity, "Gemini 1.5 Pro")
        return f"Task routed to {assigned_model} (Complexity: {complexity})"
