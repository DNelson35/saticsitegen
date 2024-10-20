import unittest

from src.leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
  def test_create_node_raise(self):
    with self.assertRaises(ValueError):
      LeafNode()
    with self.assertRaises(ValueError):
      LeafNode("b")

  def test_create_node_pass(self):
    node = LeafNode("a", "click", {"href": "https://www.google.com"})
    node2 = LeafNode(None,"this is a test", None)
    self.assertIsInstance(node, LeafNode)
    self.assertIsInstance(node2, LeafNode)

  def test_to_html(self):
    node = LeafNode("a", "click", {"href": "https://www.google.com"})
    node2 = LeafNode(None,"this is a test", None)
    html_tag = node.to_html()
    string = node2.to_html()
    self.assertEqual(html_tag, '''<a href="https://www.google.com">click</a>''')
    self.assertEqual(string, "this is a test")

