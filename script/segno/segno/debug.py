from segno_grammarListener import segno_grammarListener

class debug_listener(segno_grammarListener):
  def __init__(self, parser):
    self.parser      = parser
    self.indentation = 0
    pass
    
  def enterEveryRule(self, ctx):
    print(('|  ' * self.indentation) + "|- " + self.parser.ruleNames[ctx.getRuleIndex()])
    self.indentation += 1
    super().enterEveryRule(ctx)
    
  def exitEveryRule(self, ctx):
    self.indentation -= 1
    super().exitEveryRule(ctx)
    
  def visitTerminal(self, ctx):
    print(('|  ' * (self.indentation-1)) + '|- "' + ctx.getText() + '"')
    super().visitTerminal(ctx)
