from langchain_community.llms import Ollama
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent
from langchain.agents import AgentType

#LLM Model
llm = Ollama(model = "llama3")

#MySQL Database Connection
mysql_uri = f"mysql+mysqlconnector://root:root123@localhost:3306/chinook"
db = SQLDatabase.from_uri(mysql_uri)
db.get_usable_table_names()

# Langchain SQL agent
agent_executor = create_sql_agent(llm, db = db, agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose = True)
agent_executor.invoke("how many albums we have in database ?")
# agent_executor.invoke("How many different Artists are in the database?")
