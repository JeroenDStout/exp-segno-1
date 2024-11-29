from .generator_base import generator_base
from .sg_translation_unit import sg_translation_unit
from .sg_field            import sg_field

from overrides import override
import json

class generator_cxx_decl(generator_base):
  def __init__(self, output_method):
    super().__init__(output_method)
    
  @override
  def write_document_head(self, translation_unit:sg_translation_unit):
    self.output.stack_push_comment_cxx()
    self.write_generated_header()
    self.output.stack_pop()
    self.output.space_block([ ("*", 2) ])
    
  @override
  def write_document_tail(self, translation_unit:sg_translation_unit):
    self.output.space_block([ ("*", 2) ])
    self.output.end_space_block()
    self.output.stack_push_comment_cxx()
    self.output.write_line("This file was generated from the following segno description:")
    self.output.write_lines(json.dumps(translation_unit.create_debug_dict(), indent=2).split('\n'))
    self.output.stack_pop()
    
  @override
  def write_translation_unit_head(self, translation_unit:sg_translation_unit):
    self.output.stack_push_namespace_cxx("segno")
    
  @override 
  def write_translation_unit_tail(self, translation_unit:sg_translation_unit):
    self.output.stack_pop_namespace_cxx()
    
  @override
  def write_translation_unit_field_block_head(self, translation_unit:sg_translation_unit):
    self.output.stack_push_struct_cxx("fields_row")
    
  @override
  def write_translation_unit_field_block_tail(self, translation_unit:sg_translation_unit):
    self.output.space_block([ ("struct_end", 0), ])
    self.output.stack_pop_struct_cxx()
  
  @override
  def write_translation_unit_field(self, field:sg_field):
    self.output.write_line(field.sg_typename.sg_identifier.name + " " + field.sg_identifier.name + ";")
