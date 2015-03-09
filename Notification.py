from datetime import datetime
import Utils


class Notification(object):
  def __init__(self):
    self.title = ""
    self.description = ""
    self.action = ""
    self.time = ""
    self.id = -1

  def create_static(self):
    self.title = "New apartment"
    self.description = "is now available to provide service"
    self.action = "Tap to sign as a reviewer"
    self._post_time = datetime.now()
    self.post_time = self._post_time.strftime('%Y-%m-%dT%H:%M:%S')
    self.id = 0

  def update_data(self):
    self.time = Utils.pretty_date(self._post_time)

  def get_json(self):
    return self.__dict__