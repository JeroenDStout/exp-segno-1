from .sg_field import *

class sg_translation_unit():
  def __init__(self):
    self.sg_fields = []
  
  def create_debug_string(self):
    return "{ fields: [ " + ", ".join([ e.create_debug_string() for e in self.sg_fields ]) + " ] }"

class sg_translation_unit_ctx():
  def __init__(self):
    self.sg_translation_unit = sg_translation_unit()
    pass

  def exit_field(self, ctx:sg_field_ctx):
    self.sg_translation_unit.sg_fields.append(ctx.sg_field)
    pass
  
  def create_debug_string(self):
    return "{ translation_unit: " + self.sg_translation_unit.create_debug_string() + " }"
