import json
import asyncio
from app.main import agent

async def evaluate():
    with open("eval/dataset.json") as f:
        data = json.load(f)

    correct = 0

    for item in data:
        result = await agent.run(item["query"])
        if item["expected"] in str(result):
            correct += 1

    print("Success Rate:", correct / len(data))

if __name__ == "__main__":
    asyncio.run(evaluate())
