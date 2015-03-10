from pymongo import MongoClient
import datetime
from Agent import Agent
import json
from collections import namedtuple

client = None
db = None


class DbAgents(object):
  def __init__(self):
    global client,db
    if client == None:
      client = MongoClient('localhost', 27017)
    if client != None and db == None:
      db = client['test-db']

  def get_agents(self):
    global db
    my_agents = []
    for agent in db.agents.find():
      my_agents.append(agent)
    return my_agents


  def create_static(self):
    global db
    static_agent = Agent()
    static_agent.create_static_agent()

    agents = db.agents
    print agents.count()
    agent = agents.save(static_agent.get_json())
    print agents.find_one()

  def update_agent(self,updated_agent):
    global db
    agents = db.agents
    for agent in agents.find({"agent_id":updated_agent.agent_id}):
      print agent
      id = agent['_id']
    agents.update({'_id' : id}, updated_agent.get_json(), False)

  def update_agent_json(self, id, document):
    global db
    agents = db.agents
    for agent in agents.find({"agent_id":id}):
      print agent
      id = agent['_id']
    agents.update({'_id' : id}, document, False)

if __name__ == "__main__":
  x = DbAgents()
  static_agent = Agent()
  static_agent.create_static_agent()
  x.update_agent(static_agent)

