import unittest
from src.utils.helpers import split_nodes_delimiter, split_node_images, split_node_links
from src.textnode import TextNode, TextType

class TestSplitNodesDelimiter(unittest.TestCase):

  def setUp(self):
    self.test_cases = [
      (
        ([TextNode("This is text with a `code block` word", TextType.TEXT)], "`", TextType.CODE),
        [
          TextNode("This is text with a ", TextType.TEXT),
          TextNode("code block", TextType.CODE),
          TextNode(" word", TextType.TEXT),
        ]
      ),
      (
        ([TextNode("this is text with a few **bold** text **words**", TextType.TEXT)], "**", TextType.BOLD),
        [
          TextNode("this is text with a few ", TextType.TEXT),
          TextNode("bold", TextType.BOLD),
          TextNode(" text ", TextType.TEXT),
          TextNode("words", TextType.BOLD),
          TextNode("", TextType.TEXT)
        ]
      ),
      (
        ([
          TextNode("this is text with a few **bold** text **words**", TextType.TEXT), TextNode("This is text with a **code block** word", TextType.TEXT)
        ], "**", TextType.BOLD),
        [
          TextNode("this is text with a few ", TextType.TEXT),
          TextNode("bold", TextType.BOLD),
          TextNode(" text ", TextType.TEXT),
          TextNode("words", TextType.BOLD),
          TextNode("", TextType.TEXT),
          TextNode("This is text with a ", TextType.TEXT),
          TextNode("code block", TextType.BOLD),
          TextNode(" word", TextType.TEXT),
        ]
      ),
      (
        ([TextNode("This is text with a code blo*ck* word", TextType.TEXT)], "*", TextType.ITALIC),
        [
          TextNode("This is text with a code blo", TextType.TEXT),
          TextNode("ck", TextType.ITALIC),
          TextNode(" word", TextType.TEXT),
        ]
      ),
    ]

    self.test_fail_cases = [
      ([TextNode("This is text with a code block* word", TextType.TEXT)], "*", TextType.ITALIC),
    ]

    self.test_split_images = [
      (
        [
          TextNode("This is text with an image ![rick roll](https://i.imgur.com/aKaOqIh.gif) and another ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", TextType.TEXT),
        ],
        [
          TextNode("This is text with an image ", TextType.TEXT),
          TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
          TextNode(" and another ", TextType.TEXT),
          TextNode("obi wan", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
        ]
      ),
    ]

    self.test_split_links = [
      (
        [
          TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",TextType.TEXT,)
        ],
        [
          TextNode("This is text with a link ", TextType.TEXT),
          TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
          TextNode(" and ", TextType.TEXT),
          TextNode("to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"),
        ]
      ),
    ]

  def test_split_nodes(self):
    for test, expected in self.test_cases:
      self.assertEqual(split_nodes_delimiter(test[0],test[1],test[2]), expected)

  def test_invalid_syntax(self):
    for test in self.test_fail_cases:
      with self.assertRaises(Exception):
        split_nodes_delimiter(test[0], test[1], test[2])

  def test_split_node_links(self):
    for test, expected in self.test_split_links:
      self.assertEqual(split_node_links(test), expected)

  def test_split_image_links(self):
    for test, expected in self.test_split_images:
      self.assertEqual(split_node_images(test), expected)