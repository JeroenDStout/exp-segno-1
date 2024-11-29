import json
from .sg_field import *

class sg_translation_unit():
  def __init__(self):
    self.sg_fields = []
  
  def create_debug_dict(self):
    return { "fields" : [ e.create_debug_dict() for e in self.sg_fields ] }

class sg_translation_unit_ctx():
  def __init__(self):
    self.sg_translation_unit = sg_translation_unit()
    pass

  def exit_field(self, ctx:sg_field_ctx):
    self.sg_translation_unit.sg_fields.append(ctx.sg_field)
    pass
  
  def get_short_name(self):
    return "trunit"
  
  def create_debug_dict(self):
    return { "translation_unit" : self.sg_translation_unit.create_debug_dict() }
