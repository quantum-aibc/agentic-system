class Planner:
    async def create_plan(self, state):
        query = state["query"]

        # simple heuristic plan (replace with LLM later)
        if "date" in query:
            return {"steps": [{"tool": "datetime_tool", "input": "", "parallel": False}]}
        if "*" in query or "+" in query:
            return {"steps": [{"tool": "calculator", "input": query, "parallel": False}]}

        return {"steps": [{"tool": "web_search", "input": query, "parallel": False}]}
