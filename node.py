class Node:
  def __init__(self, value, pointers=0, next_value=None):
    self.value = value
    self.pointers = pointers
    if self.pointers > 1:
      self.next_value = [None for i in range(pointers)]
      self.next_value[0] = next_value
    elif self.pointers == 1:
      self.next_value = next_value
    else:
      self.next_value = None

  def set_next_value(self, value, index=0):
    if self.pointers == 1:
      self.next_value = value
    elif self.pointers > 1:
      self.next_value[index] = value

  def set_value(self, value):
    self.value = value 

  def get_next_value(self):
    return self.next_value

  def get_value(self):
    return self.value 
