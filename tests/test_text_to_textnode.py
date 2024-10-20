import unittest 

from src.textnode import TextNode, TextType
from src.utils.helpers import text_to_textnodes

class TestTextToTextNodes(unittest.TestCase):
  def setUp(self):
    self.test_cases = [
      (
        "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)",
        [
          TextNode("This is ", TextType.TEXT),
          TextNode("text", TextType.BOLD),
          TextNode(" with an ", TextType.TEXT),
          TextNode("italic", TextType.ITALIC),
          TextNode(" word and a ", TextType.TEXT),
          TextNode("code block", TextType.CODE),
          TextNode(" and an ", TextType.TEXT),
          TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
          TextNode(" and a ", TextType.TEXT),
          TextNode("link", TextType.LINK, "https://boot.dev"),
        ]
      )
    ]

  def test_text_to_textnode(self):
    for text, expected in self.test_cases:
      self.assertEqual(text_to_textnodes(text), expected)