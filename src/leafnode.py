from htmlnode import HTMLNode

class LeafNode(HTMLNode):
  def __init__(self, tag=None, value=None, props=None):
    super().__init__(tag, value, None, props)
    if value == None:
      raise ValueError("All leaf nodes must have a value")
    
  def to_html(self):
    if self.tag == None:
      return f"{self.value}"
    return f"""<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"""
  
  