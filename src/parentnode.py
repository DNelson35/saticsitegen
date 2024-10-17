from .htmlnode import HTMLNode

class ParentNode(HTMLNode):
  def __init__(self, tag=None, children=None, props=None):
    super().__init__(tag, None, children, props)
    if self.children == None or not self.children:
      raise ValueError("parent node must have children")
    if self.tag == None:
      raise ValueError("parent node must have a tag")
    
  def to_html(self):
    result = ""
    for child in self.children:
      result += child.to_html()
    return f"""<{self.tag}{self.props_to_html()}>{result}</{self.tag}>"""
      
