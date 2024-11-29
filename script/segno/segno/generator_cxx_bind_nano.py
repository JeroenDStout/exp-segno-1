from .generator_base      import *
from .sg_translation_unit import sg_translation_unit

from overrides import override
import json

class generator_cxx_bind_nano(generator_base):
  def __init__(self, output_method):
    super().__init__(output_method)
    
  @override
  def write_document_head(self, translation_unit:sg_translation_unit):
    self.output.stack_push_comment_cxx()
    self.write_generated_header()
    self.output.stack_pop()
    self.output.space_block([ ("*", 2) ])
    
  @override
  def write_translation_unit_head(self, translation_unit:sg_translation_unit):
    self.output.stack_push_namespace_cxx("segno")
    
  @override  
  def write_translation_unit_tail(self, translation_unit:sg_translation_unit):
    self.output.stack_pop_namespace_cxx()
    
  @override
  def write_translation_unit_field_block_head(self, translation_unit:sg_translation_unit):
    self.output.stack_push_fn_cxx("nb_field_row", [ "nanobind::module_ &m" ])
    self.output.write_line('nanobind::class_<fields_row>(m, "fields_row")')
    self.output.stack_push_indent(2)
    self.output.write_line('.def(nanobind::init<>())')
    
  @override
  def write_translation_unit_field_block_tail(self, translation_unit:sg_translation_unit):
    self.output.stack_pop()
    self.output.write_line(';')
    self.output.stack_pop_fn_cxx()
  
  @override
  def write_translation_unit_field(self, field:sg_field):
    self.output.write_line(f'.def_rw("{field.sg_identifier.name}", &fields_row::{field.sg_identifier.name})')
    
