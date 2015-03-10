from Contact import Contact
from Notification import Notification
class Agent(object):

  def __init__(self):
    # agent private details
    self.contact = Contact()
    # agent system details
    self.agent_id = ""
    self.active = ""
    self.level = ""

  def get_rank(self):
    # Get the rank calculation
    pass

  def get_level(self):
    # Get the level calculation
    pass

  def get_balance(self):
    # Get the balance calculation
    pass

  def get_apartments_in_process(self):
    # Get the number of apartments in that are currently being managed by the agent
    pass

  def get_notifications(self):
    # Get the agents notifications (a list)
    pass

  def get_pending_issues(self):
    # Get the agents urging issues
    pass

  def get_schedule_requests(self):
    # Get the agents schedule requests
    pass

  def get_messages(self):
    # Get the agents messages(include the pending issues)
    pass

  def create_static_agent(self):
    print "Creating static agent"
    self.agent_id = 0
    self.active = "Active"
    self.rank = "8.9(374)"
    self.level = 4
    self.balance = "$7303"
    self.apartments_in_process = 4
    self.notifications = []
    static_notification = Notification()
    static_notification.create_static()
    self.notifications.append(static_notification)
    static_contact = Contact()
    static_contact.create_static_contact()
    self.contact = static_contact

  def update_data(self):
    for notification in self.notifications:
      notification.update_data()

  def get_json(self):
    val = self.__dict__.copy()
    json_notifications = []
    for notification in self.notifications:
      json_notifications.append(notification.get_json())
    val["notifications"] = json_notifications
    val["contact"] = self.contact.get_json()
    return val


