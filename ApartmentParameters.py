from Contact import Contact

# A review with parameters of the apartment
class ApartmentParameters:
  def __init__(self):
    self.reviewer = Contact()
    self.parameters = {}

  def add_parameter(self, parameter, score):
    # Should be smarter one day
    self.parameters[parameter] = score