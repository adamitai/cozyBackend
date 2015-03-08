import os
from tornado import ioloop,web
from pymongo import MongoClient
import json
from bson import json_util
from bson.objectid import ObjectId
from Agent import Agent



class AgentHandler(web.RequestHandler):
    agents = None
    static = True

    def init_agents(self):
      if self.agents == None:
        if self.static:
          self.create_static_agents()
        else:
          #agents = get_from_db()
          pass

    def get(self):
      self.init_agents()
      self.set_header("Content-Type", "application/json")
      self.write(json.dumps(list(self.agents),default=json_util.default))


    def post(self):
        print('story created with id ' + str(self.request.body))
        self.set_header("Content-Type", "application/json")
        self.set_status(201)

    def create_static_agents(self):
      self.agents = []
      static_agent = Agent()
      static_agent.create_static_agent()
      self.agents.append(static_agent.get_json())