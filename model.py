from generate_power_set import * 
from unpacking_list import * 
from node import * 

class Model:
  def __init__(self, labels):
    self.elem_num = len(list(labels))
    self.labels = [Node(labels[i], 2) for i in range (self.elem_num)]
    self.label_nodes = Node(self.labels, 2)
    self.power = generate_power_set(self.labels)
    next_measured_effect = Node(self.power[1], 2)
    self.label_nodes.set_next_value(next_measured_effect)
    for i in range(1, len(self.power)):
      if i < len(self.power) - 1:
        next_measured_effect.set_next_value(Node(self.power[i+1], 2))
        next_measured_effect.set_next_value([], 1)
        next_measured_effect = next_measured_effect.get_next_value()[0]
    self.label_nodes.set_next_value([], 1)
  def set_elements(self, label, elem_labels):
    for i in range(len(self.label_nodes.get_value())):
      if label == self.label_nodes.get_value()[i].get_value():
        self.label_nodes.get_value()[i].set_next_value(Model(elem_labels), 1)
        self.label_nodes.get_next_value()[1].append(Model(elem_labels))
        self.label_nodes.get_next_value()[1] = unpack_nested_list(self.label_nodes.get_next_value()[1])
        next_measured_effect = self.label_nodes.get_next_value()[0]
        for i in range(1, len(self.power)):
          for j in next_measured_effect.get_value():
            if label == j.get_value():
              next_measured_effect.get_next_value()[1].append(Model(elem_labels))
              next_measured_effect.get_next_value()[1] = unpack_nested_list(next_measured_effect.get_next_value()[1])
              break
          next_measured_effect = next_measured_effect.get_next_value()[0]
          if next_measured_effect.get_value() == []: 
            break
        break
    self.labels = self.label_nodes.get_value()
  def get_sub_elements(self, label):
    for i in range(len(self.labels)):
      if self.labels[i].get_value() == label:
        return self.labels[i].get_next_value()[1]
  def get_labels(self):
    self.labels = self.label_nodes.get_value()
    return [self.labels[i].get_value() for i in range(len(self.labels))] 
  def shift_measurable_space(self): 
    self.label_nodes = self.label_nodes.get_next_value()[0]
  def get_label_node(self): 
    return self.label_nodes
  def get_all_sub_elem_labels(self): 
    ls = [self.label_nodes.get_next_value()[1][i].get_labels() for i in range(len(self.label_nodes.get_next_value()[1]))]
    return unpack_nested_list(ls) 
  def get_all_sub_elem(self): 
    return self.label_nodes.get_next_value()[1]
  def get_sub_model_by_label(self, label): 
    for i in range(len(self.label_nodes.get_value())): 
      if label == self.label_nodes.get_value()[i].get_value(): 
        return self.label_nodes.get_value()[i].get_next_value()[1]
