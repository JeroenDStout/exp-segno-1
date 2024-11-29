from .generator_base import *
from .sg_translation_unit import sg_translation_unit

from overrides import override
import json

class generator_cxx_cpp(generator_base):
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
