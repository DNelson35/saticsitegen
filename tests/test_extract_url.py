import unittest

from src.utils.helpers import extract_markdown_images, extract_markdown_links

class TestExtractUrl(unittest.TestCase):

  def setUp(self):
    self.image_test_cases = [
      (
        "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)", 
        [
          ("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")
        ]
      ),
    ]

    self.link_test_cases = [
      ("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")])
    ]


  def test_extract_image_url(self):
    for text, expected in self.image_test_cases:
      self.assertEqual(extract_markdown_images(text), expected)

  def test_extract_link_url(self):
    for text, expected in self.link_test_cases:
      self.assertEqual(extract_markdown_links(text), expected)