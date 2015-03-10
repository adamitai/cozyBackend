from DbAgents import DbAgents
from Notification import Notification


def NotifyAllAgents():
  agents = DbAgents()
  x = Notification()
  x.create_static()
  for agent in agents.get_agents():
    agent["notifications"].insert(0,x.get_json())
    agents.update_agent_json(agent["_id"],agent)


NotifyAllAgents()