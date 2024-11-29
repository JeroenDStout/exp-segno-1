from segno_grammarListener import segno_grammarListener
from segno_grammarParser   import segno_grammarParser

from .sg_translation_unit  import *
from .sg_field             import *
from .sg_operator          import *
from .sg_identifier        import *
from .sg_pass              import *
from .sg_typename          import *

from overrides import override

class sg_listener(segno_grammarListener):
  def __init__(self, parser):
    self.parser           = parser
    self.stack            = []
    self.debug_mode       = False
    self.translation_unit = None
    pass
  
  def stack_push(self, element):
    self.stack.append(element)
    if self.debug_mode:
      print(" | ".join([ e.get_short_name() for e in self.stack ]))
  
  def stack_pop(self):
    if self.debug_mode:
      print(" | ".join([ e.get_short_name() for e in self.stack ]) + " " + json.dumps(self.stack[-1].create_debug_dict(), indent=2))
    return self.stack.pop()
    
  @override
  def enterProg(self, ctx:segno_grammarParser.ProgContext):
    self.stack_push(sg_translation_unit_ctx())
    
  @override
  def exitProg(self, ctx:segno_grammarParser.ProgContext):
    self.translation_unit = self.stack_pop()
    
  @override
  def enterField_def(self, ctx:segno_grammarParser.Field_defContext):
    self.stack_push(sg_field_ctx())
    
  @override
  def exitField_def(self, ctx:segno_grammarParser.Field_defContext):
    identifier_ctx:sg_field_ctx = self.stack_pop()
    self.stack[-1].exit_field(identifier_ctx)
    
  @override
  def enterOperator_def(self, ctx:segno_grammarParser.Operator_defContext):
    self.stack_push(sg_operator_ctx())
    
  @override
  def exitOperator_def(self, ctx:segno_grammarParser.Operator_defContext):
    self.stack_pop()
    
  @override
  def enterPass_def(self, ctx:segno_grammarParser.Pass_defContext):
    self.stack_push(sg_pass_ctx())
    
  @override
  def exitPass_def(self, ctx:segno_grammarParser.Pass_defContext):
    self.stack_pop()
    
  @override
  def enterIdentifier(self, ctx:segno_grammarParser.IdentifierContext):
    self.stack_push(sg_identifier_ctx())
    
  @override
  def exitIdentifier(self, ctx:segno_grammarParser.IdentifierContext):
    identifier_ctx = self.stack_pop()
    self.stack[-1].exit_identifier(identifier_ctx)
    
  @override
  def enterTypename(self, ctx:segno_grammarParser.TypenameContext):
    self.stack_push(sg_typename_ctx())
    
  @override
  def exitTypename(self, ctx:segno_grammarParser.TypenameContext):
    typename_ctx = self.stack_pop()
    self.stack[-1].exit_typename(typename_ctx)
    
  @override
  def enterIdentifier_name(self, ctx:segno_grammarParser.Identifier_nameContext):
    self.stack[-1].enter_identifier_name(ctx)
