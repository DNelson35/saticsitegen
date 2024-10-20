import unittest
from src.htmlnode import HTMLNode

class TestHtmlNode(unittest.TestCase):

  def setUp(self):
    self.node = HTMLNode("<h1>", "testing", ["node1", "node2", "node3"], {"href": "https://www.testing.com", "target": "_blank"})

  def test_create_html_node(self):
    self.assertIsInstance(self.node, HTMLNode, f"Expecting node to be instance of HTMLNode got {type(self.node)}")

  def test_create_empty_node(self):
    node = HTMLNode()
    self.assertIsInstance(node, HTMLNode, f"Expecting node to be instance of HTMLNode got {type(self.node)}")
  
  def test_props_to_html(self):
    prop_str = self.node.props_to_html()
    expected = ' href="https://www.testing.com" target="_blank"'
    self.assertEqual(prop_str, expected, f"Expected properties string '{expected}' but got '{prop_str}'" )
    
