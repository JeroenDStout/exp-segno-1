from .sg_identifier import *

class sg_operator():
  def __init__(self):
    self.sg_identifier = sg_identifier()
  
  def create_debug_string(self):
    return "{ identifier: " + self.sg_identifier.create_debug_string() + " }"

class sg_operator_ctx():
  def __init__(self):
    self.sg_operator = sg_operator()
    pass

  def exit_identifier(self, ctx):
    self.sg_operator.sg_identifier = ctx.sg_identifier
    pass
  
  def create_debug_string(self):
    return "{ operator: " + self.sg_operator.create_debug_string() + " }"
