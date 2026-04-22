from datetime import datetime

class DateTimeTool:
    async def run(self, _):
        return {"tool": "datetime_tool", "result": str(datetime.now())}
