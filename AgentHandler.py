from tornado import ioloop,web
import json
from bson import json_util
from Agent import Agent
import Static
import DbAgents

agents = None

class AgentHandler(web.RequestHandler):

    def init_agents(self):
      global agents
      self.static = False
      if Static.Agents == None:
        if self.static:
          self.create_static_agents()
        elif agents == None:
          agents = DbAgents.DbAgents()


    def get(self):
      global agents
      self.init_agents()
      #self.update_agents()
      self.set_header("Content-Type", "application/json")
      self.write(json.dumps(list(agents.get_agents()),default=json_util.default))

      #self.write(json.dumps(list(self.get_json()),default=json_util.default))


    def post(self):
        print('story created with id ' + str(self.request.body))
        self.set_header("Content-Type", "application/json")
        self.set_status(201)

    def create_static_agents(self):
      Static.Agents = []
      static_agent = Agent()
      static_agent.create_static_agent()
      Static.Agents.append(static_agent)

    def update_agents(self):
      for agent in Static.Agents:
        agent.update_data()

    def get_json(self):
      json_agents = []
      for agent in Static.Agents:
        json_agents.append(agent.get_json())
      return json_agents