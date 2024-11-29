class writer_ctx():
  def __init__(self, output_method):
    self.output     = output_method
    self.stack      = []
    self.line_space = {}

  def write_line(self, line):
    for e in self.stack:
      self.output.write(e)
      
    self.output.write(line)
    self.output.write("\n")
    
  def write_lines(self, lines):
    for l in lines:
      self.write_line(l)
      
  def stack_pop(self):
    self.stack.pop()
      
  def stack_push_indent(self, amount):
    self.stack.append(" " * amount) 
      
  def stack_push_comment_cxx(self):
    self.stack.append("// ") 
      
  def stack_push_namespace_cxx(self, namespace):
    self.space_block([ ("*", 2) ])
    self.end_space_block("namespace_start")
    self.write_line("namespace " + namespace + " {")
    self.space_block([ ("*", 1) ])
    self.stack.append("    ") 
      
  def stack_pop_namespace_cxx(self):
    self.space_block([ ("*", 1) ])
    self.end_space_block("namespace_end")
    self.stack.pop() 
    self.write_line("}")
    self.space_block([ ("*", 2), ("struct_start", 1) ])
      
  def stack_push_struct_cxx(self, identifier):
    self.space_block([ ("*", 1) ])
    self.end_space_block("struct_start")
    self.write_line("struct " + identifier + " {")
    self.stack.append("    ") 
      
  def stack_pop_struct_cxx(self):
    self.space_block([ ("*", 1), ])
    self.end_space_block("struct_end")
    self.stack.pop() 
    self.write_line("};")
    self.space_block([ ("*", 2), ( "namespace_end", 1) ])
      
  def stack_push_fn_cxx(self, identifier, arg=[], ret="void"):
    self.space_block([ ("*", 1) ])
    self.end_space_block("fn_start")
    if ret == "void":
      self.write_line("void " + identifier + "(" + ", ".join(arg) + ") {")
    else:
      self.write_line("auto " + identifier + "(" + ", ".join(arg) + ") -> " + ret + " {")
    self.stack.append("    ") 
      
  def stack_pop_fn_cxx(self):
    self.end_space_block("fn_end")
    self.stack.pop() 
    self.write_line("}")
    self.space_block([ ("*", 2), ( "namespace_end", 1) ])
    
  def space_block(self, space_types):
    for st in space_types:
      self.line_space[st[0]] = max(self.line_space.get(st[0], 0), st[1])
    
  def end_space_block(self, space_type="*"):
    count = self.line_space.get(space_type, self.line_space.get("*", 0))
    for _ in range(count):
      self.output.write("\n")
    self.line_space = {}