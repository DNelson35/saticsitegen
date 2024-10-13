class TextNode():
  def __init__(self, text, text_type, url=None):
    self.text = text
    self.text_type = text_type
    self.url = url

  def __eq__(self, node1):
    return (
      isinstance(node1, TextNode) and
      self.text == node1.text and
      self.text_type == node1.text_type and
      self.url == node1.url
    )

  def __repr__(self):
    return f"TextNode({self.text}, {self.text_type}, {self.url})"
  