import re
from ..textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes: list[TextNode], delim, text_type: TextType):
  result_list = []
  for node in old_nodes:
    if node.text_type != TextType.TEXT:
      result_list.append(node)
    else:
      split_text = node.text.split(delim)
      if len(split_text) % 2 == 0:
        raise Exception("invalid markdown syntax")
      result_list.extend(list(map(lambda text_chunk: _get_node(text_chunk[1], text_chunk[0], text_type) ,enumerate(split_text))))
        
  return result_list
# may need to remove any blank text nodes form list like this [node for node in nodes if node.text]

def _get_node(text_chunk, index, text_type):
    if index % 2 == 0:
      return TextNode(text_chunk, TextType.TEXT)
    else:
      return TextNode(text_chunk, text_type)


# this text **isword** and needs **more** stu**ff**
# ["this text ", "isword", " and needs ", "more", " stu", "ff", ""]

# i could make this recursive to deal with all delimiters in the source text
# this could work by making a map of possible delims and on each call detecting which delim is present in the test and then passing the text type to the call.
# current set up would have to pass the array in multiple times to deal with diffrent delims

def extract_markdown_images(txt):
  image_url = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", txt)
  return image_url

def extract_markdown_links(txt):
  link_url = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", txt)
  return link_url


def split_node_images(old_nodes: list[TextNode]):
  new_nodes = []
  for old_node in old_nodes:
    if old_node.text_type != TextType.TEXT:
      new_nodes.append(old_node)
      continue
    original_text = old_node.text
    images = extract_markdown_images(original_text)
    if len(images) == 0:
      new_nodes.append(old_node)
      continue
    for image in images:
      sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
      if len(sections) != 2:
        raise ValueError("Invalid markdown, image section not closed")
      if sections[0] != "":
        new_nodes.append(TextNode(sections[0], TextType.TEXT))
      new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1],))
      original_text = sections[1]
    if original_text != "":
      new_nodes.append(TextNode(original_text, TextType.TEXT))
  return new_nodes

def split_node_links(old_nodes):
  new_nodes = []
  for old_node in old_nodes:
    if old_node.text_type != TextType.TEXT:
      new_nodes.append(old_node)
      continue
    original_text = old_node.text
    links = extract_markdown_links(original_text)
    if len(links) == 0:
      new_nodes.append(old_node)
      continue
    for link in links:
      sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
      if len(sections) != 2:
        raise ValueError("Invalid markdown, link section not closed")
      if sections[0] != "":
        new_nodes.append(TextNode(sections[0], TextType.TEXT))
      new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
      original_text = sections[1]
    if original_text != "":
      new_nodes.append(TextNode(original_text, TextType.TEXT))
  return new_nodes

def text_to_textnodes(txt):
  text_node = TextNode(txt, TextType.TEXT)
  node_list = split_nodes_delimiter([text_node], '**', TextType.BOLD)
  node_list = split_nodes_delimiter(node_list, '*', TextType.ITALIC)
  node_list = split_nodes_delimiter(node_list, "`", TextType.CODE)
  node_list = split_node_images(node_list)
  node_list = split_node_links(node_list)
  return node_list
