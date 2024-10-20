from enum import Enum
from .leafnode import LeafNode

class TextType(Enum):
  TEXT = "text"
  BOLD = "bold"
  ITALIC = "italic"
  CODE =  "code"
  LINK = "link"
  IMAGE = "image"

class TextNode():
  def __init__(self, text, text_type: TextType, url=None):
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
  
  def text_node_to_html_node(self):
    match self.text_type:
      case TextType.TEXT:
        return LeafNode(None, self.text)
      case TextType.BOLD:
        return LeafNode("b", self.text)
      case TextType.ITALIC:
        return LeafNode("i", self.text)
      case TextType.CODE:
        return LeafNode("code", self.text)
      case TextType.LINK:
        return LeafNode("a", self.text, {"href": self.url})
      case TextType.IMAGE:
        return LeafNode("img", "", {"src": self.url, "alt": self.text})
      case _:
        raise Exception(f"Unknown TextType: {self.text_type}")
      
  

  