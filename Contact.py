from Address import Address

class Contact(object):
  def __init__(self):
    self.first_name = ""
    self.last_name = ""
    self.address = ""
    self.phone = ""
    self.email = ""
    self.image = ""

  def create_static_contact(self):
    self.first_name = "Real"
    self.last_name = "Person"
    self.phone = "972526666666"
    self.email = "real.person@gmail.com"
    self.image = "http://www.google.com"
    static_address = Address()
    static_address.create_static_address()
    self.address = static_address

  def get_json(self):
    val = self.__dict__.copy()
    val["address"] = self.address.get_json()
    return val