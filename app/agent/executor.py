import asyncio

class Executor:
    def __init__(self, tools):
        self.tools = tools

    async def execute(self, plan):
        tasks = []

        for step in plan["steps"]:
            tool = self.tools[step["tool"]]

            if step.get("parallel"):
                tasks.append(tool.run(step["input"]))
            else:
                return [await tool.run(step["input"])]

        return await asyncio.gather(*tasks)
