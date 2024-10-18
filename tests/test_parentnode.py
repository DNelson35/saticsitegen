import unittest
from src.parentnode  import ParentNode
from src.leafnode import LeafNode

class TestParentNode(unittest.TestCase):

  def setUp(self):
    self.node = ParentNode(
      "p",
      [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
      ],
    )
    self.node2 = ParentNode(
      "div",
      [
        ParentNode(
          "p",
          [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),  
          ],   
        ),
        ParentNode(
          "ul",
          [
            LeafNode("li", "one", {"class": "blue"}),
            LeafNode("li", "two"),
          ],
          {
            "class": "numbers"
          }
        )
      ],
      {"class": "stylediv"}
    )

  def test_parent_node_invalid_initialization(self):
    with self.assertRaises(ValueError):
      ParentNode()

    with self.assertRaises(ValueError):
      ParentNode("div", None, {"classname": "test"})
    
    with self.assertRaises(ValueError):
      ParentNode("div", [], {"classname": "test"})

    with self.assertRaises(ValueError):
      ParentNode(None, [LeafNode("b", "Bold text")], {"classname": "test"})

  def test_to_html(self):
    html = self.node.to_html()
    html2 = self.node2.to_html()
    expected_html = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
    expected_html2 = '<div class="stylediv"><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p><ul class="numbers"><li class="blue">one</li><li>two</li></ul></div>'
    
    self.assertEqual(html, expected_html)
    self.assertEqual(html2, expected_html2)
