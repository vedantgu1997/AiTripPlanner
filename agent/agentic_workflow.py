from utils.model_loader import ModelLoader
from prompt_library.prompt import SYSTEM_PROMPT
from langgraph.graph import StateGraph, MessagesState, END, START
from langgraph.prebuilt import ToolNode, tools_condition
# from tools.weather_info_tool import WeatherInfoTool
# from tools.place_search_tool import PlaceSearchTool
# from tools.expense_calculator_tool import ExpenseCalculatorTool
# from tools.currency_conversion_tool import CurrencyConversionTool


class GraphBuilder():
    def __init__(self):
        self.tools = []
        self.system_prompt = SYSTEM_PROMPT

    def agent_function(self,state: MessagesState):
        """
        Main Agent function that processes the state and returns a response.
        """
        user_question = state["messages"]
        input_question = [self.system_prompt] + user_question
        response = self.llm_with_tools.invoke(input_question)
        return {'messages': response}


    def build_graph(self):
        graphbuilder = StateGraph(MessagesState)
        graphbuilder.add_node("agent", self.agent_function)
        graphbuilder.add_node("tools", ToolNode(tools=self.tools()))
        graphbuilder.add_edge(START, "agent")
        graphbuilder.add_conditional_edges("agent", tools_condition)
        graphbuilder.add_edge("tools", "agent")
        graphbuilder.add_edge("agent", END)



    def __call__(self):
        pass