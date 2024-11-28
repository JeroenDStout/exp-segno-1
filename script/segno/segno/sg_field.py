from segno.sg_identifier import *

class sg_field():
  def __init__(self):
    self.sg_identifier = sg_identifier()
  
  def create_debug_string(self):
    return "{ identifier: " + self.sg_identifier.create_debug_string() + " }"

class sg_field_ctx():
  def __init__(self):
    self.sg_field = sg_field()
    pass

  def exit_identifier(self, ctx):
    self.sg_field.sg_identifier = ctx.sg_identifier
    pass
  
  def create_debug_string(self):
    return "{ field: " + self.sg_field.create_debug_string() + " }"
