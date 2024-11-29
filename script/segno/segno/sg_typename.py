from .sg_identifier import *

class sg_typename():
  def __init__(self):
    self.sg_identifier = sg_identifier()
  
  def create_debug_string(self):
    return "{ identifier: " + self.sg_identifier.create_debug_string() + " }"

class sg_typename_ctx():
  def __init__(self):
    self.sg_typename = sg_typename()
    pass

  def exit_identifier(self, ctx):
    self.sg_typename.sg_identifier = ctx.sg_identifier
    pass
  
  def create_debug_string(self):
    return "{ typename: " + self.sg_typename.create_debug_string() + " }"
