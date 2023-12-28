from model import * 

class Physics:
  def __init__(self, target_model):
    self.target_model = target_model
    self.target_label_node = self.target_model.get_label_node()
    self.target_state = Node({}, 1)
    self.target_state.set_next_value(self.target_label_node)
    self.target_function = Node({}, 1)
    self.target_function.set_next_value(self.target_state)

    self.elemental_states = [Node({}, 1) for i in range(len(self.target_label_node.get_value()))]
    self.elemental_functions = [Node({}, 1) for i in range(len(self.target_label_node.get_value()))]
    for i in range(len(self.elemental_states)):
      self.elemental_states[i].set_next_value(self.target_label_node.get_value()[i])
      self.elemental_functions[i].set_next_value(self.elemental_states[i])
    self.target_labels = [self.target_label_node.get_value()[i].get_value() for i in range(len(self.target_label_node.get_value()))]
    self.time = {
        'Model':[]
    }
    for label in self.target_labels: 
      self.time.update({label:[]})
  def get_target_state(self):
    return self.target_state

  def get_model_age(self):
    return len(self.time['Model'])

  def get_elemental_states(self, label):
    for i in range(len(self.elemental_states)):
      if self.elemental_states[i].get_next_value().get_value() == label:
        return self.elemental_states[i]
        break

  def update_element_property(self, label, property, state, function):
    for i in range(len(self.elemental_states)):
      if self.elemental_states[i].get_next_value().get_value() == label:
        self.elemental_states[i].get_value().update({property:state})
        self.elemental_functions[i].get_value().update({property:function})
        break

  def update_target_property(self, property, state, function):
    self.target_state.get_value().update({property:state}) 
    self.target_function.get_value().update({property:function})
  
  def element_event(self, label, property, params): 
    for i in range(len(self.elemental_states)): 
      if self.elemental_states[i].get_next_value().get_value() == label: 
        for prop in self.elemental_states[i].get_value(): 
          if prop == property:
            new_val = self.elemental_functions[i].get_value()[property](*params) 
            self.elemental_states[i].get_value().update({property:new_val})
            self.time[label].append(self.elemental_states[i]) 

  def get_history(self):
    return self.time 

  def model_event(self, property, params): 
    self.target_state.get_value().update({property:self.target_function.get_value()(*params)})
    self.time['Model'].append(self.target_state)

  def update_target_property(self, property, state, function):
    self.target_state.get_value().update({property:state}) 
    self.target_function.get_value().update({property:function})
