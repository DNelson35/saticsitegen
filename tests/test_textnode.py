import unittest

from src.textnode import TextNode


class TestTextNode(unittest.TestCase):
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

    def all_case_eq(self):
      node = TextNode("all", "cases", "equal")
      node2 = TextNode("all", "cases", "equal")
      self.assertEqual(node, node2)
    


if __name__ == "__main__":
    unittest.main()