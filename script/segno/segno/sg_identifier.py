class sg_identifier():
  def __init__(self):
    self.name = "UNNAMED_IDENTIFIER"
  
  def create_debug_dict(self):
    return { "name" : self.name }

class sg_identifier_ctx():
  def __init__(self):
    self.sg_identifier = sg_identifier()
    pass

  def enter_identifier_name(self, ctx):
    self.sg_identifier.name = ctx.getText()
    pass
  
  def get_short_name(self):
    return "identf"
  
  def create_debug_dict(self):
    return { "identifier" : self.sg_identifier.create_debug_dict() }
 
