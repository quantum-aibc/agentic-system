class Agent:
    def __init__(self, planner, executor, reflector, budget):
        self.planner = planner
        self.executor = executor
        self.reflector = reflector
        self.budget = budget
        self.max_steps = 5

    async def run(self, query):
        state = {"query": query, "steps": []}

        for _ in range(self.max_steps):
            if self.budget.exceeded():
                return {"error": "Budget exceeded"}

            plan = await self.planner.create_plan(state)
            observations = await self.executor.execute(plan)
            decision = await self.reflector.reflect(state, observations)

            state["steps"].append({
                "plan": plan,
                "observations": observations,
                "decision": decision
            })

            if decision["done"]:
                return {"answer": decision["answer"], "steps": state["steps"]}

        return {"error": "Max steps reached"}
