from .writer_ctx import writer_ctx
from . import sg_translation_unit as sg_translation_unit
from . import sg_field            as sg_field

from datetime import datetime

class generator_base():
  def __init__(self, output_method):
    self.output:writer_ctx = output_method
  
  def write_document(self, translation_unit:sg_translation_unit):
    self.write_document_head(translation_unit)
    self.write_translation_unit(translation_unit)
    self.write_document_tail(translation_unit)
    
  def write_document_head(self, translation_unit:sg_translation_unit):
    pass
    
  def write_document_tail(self, translation_unit:sg_translation_unit):
    pass
  
  def write_translation_unit(self, translation_unit:sg_translation_unit):
    self.write_translation_unit_head(translation_unit)
    self.write_translation_unit_tail(translation_unit)
    
  def write_translation_unit_head(self, translation_unit:sg_translation_unit):
    pass
    
  def write_translation_unit_tail(self, translation_unit:sg_translation_unit):
    pass
  
  def write_generated_header(self):
    now     = datetime.now()
    now_str = now.strftime('%Y-%m-%d %H:%M:%S')

    self.output.write_line( "***************************************************************")
    self.output.write_line( "*                                                             *")
    self.output.write_line( "*          This file was automatically generated on           *")
    self.output.write_line(f"*                     {     now_str     }                     *")
    self.output.write_line( "*                  Please do not edit by hand                 *")
    self.output.write_line( "*                                                             *")
    self.output.write_line( "***************************************************************")