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
      
  def stack_push_comment_cxx(self):
    self.stack.append("// ") 
    
  def space_block(self, space_types):
    for st in space_types:
      self.line_space[st[0]] = max(self.line_space.get(st[0], 0), st[1])
    
  def end_space_block(self, space_type="*"):
    count = self.line_space.get(space_type, self.line_space.get("*", 0))
    for _ in range(count):
      self.output.write("\n")
    self.line_space = {}