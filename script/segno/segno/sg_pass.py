from .sg_identifier import *

class sg_pass():
  def __init__(self):
    self.sg_identifier = sg_identifier()
  
  def create_debug_string(self):
    return "{ identifier: " + self.sg_identifier.create_debug_string() + " }"

class sg_pass_ctx():
  def __init__(self):
    self.sg_pass = sg_pass()
    pass

  def exit_identifier(self, ctx):
    self.sg_pass.sg_identifier = ctx.sg_identifier
    pass
  
  def create_debug_string(self):
    return "{ pass: " + self.sg_pass.create_debug_string() + " }"
