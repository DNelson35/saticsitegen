import unittest
from htmlnode import HTMLNode

class TestHtmlNode(unittest.TestCase):
  def create_html_node(self):
    node = HTMLNode("<h1>", "testing", ["node1", "node2", "node3"], {"href": "https://www.testing.com", "target": "_blank"})
    self.assertIsInstance(node, HTMLNode)

  def create_empty_node(self):
    node = HTMLNode()
    self.assertIsInstance(node, HTMLNode)
  
  def test_props_to_html(self):
    node = HTMLNode("<h1>", "testing", ["node1", "node2", "node3"], {"href": "https://www.testing.com", "target": "_blank"})
    prop_str = node.props_to_html()
    self.assertEqual(prop_str, ' href="https://www.testing.com" target="_blank"' )
    

