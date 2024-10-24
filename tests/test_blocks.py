import unittest

from src.utils.helpers import markdown_to_blocks

class TestBlocks(unittest.TestCase):

  def setUp(self):
    self.test_cases = [
      (
        "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item""",
        [
          "# This is a heading",
          "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
          "* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        ]
      )
    ]

  def test_markdown_to_block(self):
    for test, expected in self.test_cases:
      print(expected)
      print(markdown_to_blocks(test))
      self.assertEqual(markdown_to_blocks(test), expected)