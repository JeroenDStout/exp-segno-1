from segno.sg_identifier import *
from segno.sg_typename   import *

class sg_field():
  def __init__(self):
    self.sg_identifier = sg_identifier()
    self.sg_typename   = sg_typename()
  
  def create_debug_string(self):
    return ( "{ identifier: " + self.sg_identifier.create_debug_string()
           + "; typename: " + self.sg_typename.create_debug_string()
           + " }"
           )

class sg_field_ctx():
  def __init__(self):
    self.sg_field = sg_field()
    pass

  def exit_identifier(self, ctx):
    self.sg_field.sg_identifier = ctx.sg_identifier
    pass

  def exit_typename(self, ctx):
    self.sg_field.sg_typename   = ctx.sg_typename
    pass
  
  def create_debug_string(self):
    return "{ field: " + self.sg_field.create_debug_string() + " }"
