class Calculator:
    async def run(self, query):
        try:
            result = eval(query)
            return {"tool": "calculator", "result": result}
        except:
            return {"tool": "calculator", "result": "error"}
