import unittest

from src.textnode import TextNode, TextType
from src.leafnode import LeafNode


class TestTextNode(unittest.TestCase):
    
  def setUp(self):
    self.test_cases = [
      (TextNode("Hello", TextType.TEXT), LeafNode(None, "Hello")),

      (TextNode("Bold Text", TextType.BOLD), LeafNode("b", "Bold Text")),

      (TextNode("Italic Text", TextType.ITALIC), LeafNode("i", "Italic Text")),

      (TextNode("Code Snippet", TextType.CODE), LeafNode("code", "Code Snippet")),

      (TextNode("OpenAI", TextType.LINK, "https://openai.com"), LeafNode("a", "OpenAI", {"href": "https://openai.com"})),

      (TextNode("Alt text", TextType.IMAGE, "https://example.com/image.png"), LeafNode("img", "", {"src": "https://example.com/image.png", "alt": "Alt text"}))
    ]

  def test_eq(self):
      node = TextNode("This is a text node", "bold")
      node2 = TextNode("This is a text node", "bold")
      self.assertEqual(node, node2)

  def test_text_not_eq(self):
    node = TextNode("This", "bold")
    node2 = TextNode("This is another text node", "bold")
    self.assertNotEqual(node, node2)
  
  def test_text_type_not_eq(self):
    node = TextNode("this", "italic")
    node2 = TextNode("this", "bold")
    self.assertNotEqual(node, node2)

  def test_all_case_eq(self):
    node = TextNode("all", "cases", "equal")
    node2 = TextNode("all", "cases", "equal")
    print(TextType.TEXT)
    self.assertEqual(node, node2)

  def test_textnode_to_htmlnode(self):
    for text_node, expected in self.test_cases:
      self.assertEqual(text_node.text_node_to_html_node(), expected)

  
    
