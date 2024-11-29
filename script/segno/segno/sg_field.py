from .sg_identifier import *
from .sg_typename   import *

class sg_field():
  def __init__(self):
    self.sg_identifier = sg_identifier()
    self.sg_typename   = sg_typename()
  
  def create_debug_dict(self):
    return { "identifier" : self.sg_identifier.create_debug_dict()
           , "typename"   : self.sg_typename.create_debug_dict()
           }

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
  
  def get_short_name(self):
    return "field"
  
  def create_debug_dict(self):
    return { "field" : self.sg_field.create_debug_dict() }
