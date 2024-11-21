from segno_grammarVisitor import segno_grammarVisitor

class segno_debug_visitor(segno_grammarVisitor):
  def __init__(self, parser):
    self.parser     = parser
    self.identation = 0
    
  def visitChildren(self, ctx):
    print(('  ' * self.identation) + self.parser.ruleNames[ctx.getRuleIndex()])
    self.identation += 1
    super().visitChildren(ctx)
    self.identation -= 1
    
  def visitTerminal(self, ctx):
    print(('  ' * self.identation) + '"' + ctx.getText() + '"')
    super().visitTerminal(ctx)