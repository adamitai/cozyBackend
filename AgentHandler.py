import os
from tornado import ioloop,web
from pymongo import MongoClient
import json
from bson import json_util
from bson.objectid import ObjectId
from Agent import Agent
import Static


class AgentHandler(web.RequestHandler):

    def init_agents(self):
      self.static = True
      if Static.Agents == None:
        if self.static:
          self.create_static_agents()
        else:
          #agents = get_from_db()
          pass

    def get(self):
      self.init_agents()
      self.update_agents()
      self.set_header("Content-Type", "application/json")
      self.write(json.dumps(list(self.get_json()),default=json_util.default))


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