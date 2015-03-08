from Contact import Contact
class Agent(object):
  def __init__(self):
    # agent private details
    self.contact = Contact()
    # agent system details
    self.agent_id = ""
    self.active = ""

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
    self.active = True
    static_contact = Contact()
    static_contact.create_static_contact()
    self.contact = static_contact.get_json()

  def get_json(self):
    return self.__dict__