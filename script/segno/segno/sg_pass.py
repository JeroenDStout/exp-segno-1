from .sg_identifier import *

class sg_pass():
  def __init__(self):
    self.sg_identifier = sg_identifier()
  
  def create_debug_dict(self):
    return { "identifier" : self.sg_identifier.create_debug_dict() }

class sg_pass_ctx():
  def __init__(self):
    self.sg_pass = sg_pass()
    pass

  def exit_identifier(self, ctx):
    self.sg_pass.sg_identifier = ctx.sg_identifier
    pass
  
  def get_short_name(self):
    return "pass"
  
  def create_debug_dict(self):
    return { "pass" : self.sg_pass.create_debug_dict() }
