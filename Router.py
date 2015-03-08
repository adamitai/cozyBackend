import os
from tornado import ioloop,web
from AgentHandler import AgentHandler

class IndexHandler(web.RequestHandler):
    def get(self):
        self.write("Hello World!!")

settings = {
    "template_path": os.path.join(os.path.dirname(__file__), "templates"),
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "debug" : True
}

application = web.Application([
    (r'/', IndexHandler),
    (r'/index', IndexHandler),
    (r'/api/agents',AgentHandler),
],**settings)
 
if __name__ == "__main__":
    application.listen(8888)
    ioloop.IOLoop.instance().start()