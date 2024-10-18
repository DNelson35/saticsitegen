from .htmlnode import HTMLNode

class LeafNode(HTMLNode):
  def __init__(self, tag=None, value=None, props=None):
    super().__init__(tag, value, None, props)
    if value == None:
      raise ValueError("All leaf nodes must have a value")
    
  def __repr__(self):
    return f"LeafNode({self.tag} {self.value} {self.props})"
  
  def __eq__(self, node):
    return(
      isinstance(node, LeafNode) and
      self.tag == node.tag and
      self.value == node.value and
      self.props == node.props
    )
    
  def to_html(self):
    if self.tag == None:
      return f"{self.value}"
    return f"""<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"""
  
  