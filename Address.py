class Address(object):
  def __init__(self):
    self.city = ""
    self.street = ""
    self.building_num = ""
    self.apartment_num = ""

  def create_static_address(self):
    self.city = "Tel Aviv"
    self.street = "Rotshild"
    self.building_num = 129
    self.apartment_num = 2

  def get_json(self):
    return self.__dict__