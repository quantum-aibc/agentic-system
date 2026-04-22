class Reflector:
    async def reflect(self, state, observations):
        # simple logic (replace with LLM later)
        if observations:
            return {
                "done": True,
                "answer": str(observations[0]["result"])
            }
        return {"done": False, "answer": ""}
