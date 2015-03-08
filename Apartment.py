from Contact import Contact
from Address import Address

class Apartment:
  def __init__(self):
    self.owner = Contact()
    self.agent = Contact()
    self.address = Address()