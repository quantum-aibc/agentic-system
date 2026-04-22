from app.agent.agent import Agent
from app.agent.planner import Planner
from app.agent.executor import Executor
from app.agent.reflector import Reflector
from app.agent.budget import Budget

from app.tools.calculator import Calculator
from app.tools.web_search import WebSearch
from app.tools.doc_qa import DocQA
from app.tools.kb_lookup import KBLookup
from app.tools.datetime_tool import DateTimeTool

tools = {
    "calculator": Calculator(),
    "web_search": WebSearch(),
    "doc_qa": DocQA(),
    "kb_lookup": KBLookup(),
    "datetime_tool": DateTimeTool()
}

agent = Agent(
    planner=Planner(),
    executor=Executor(tools),
    reflector=Reflector(),
    budget=Budget()
)
