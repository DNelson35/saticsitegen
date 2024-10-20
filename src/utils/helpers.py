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

def split_node_images(nodes: list[TextNode]):
  node_list = []
  
  for node in nodes:
    if node.text_type != TextType.TEXT:
      node_list.append(node)
      continue
      
    image_matches = extract_markdown_images(node.text)
      
    if not image_matches:
      node_list.append(node)
      continue
      
    text = node.text
    current_index = 0

    for alt_text, image_url in image_matches:
      markdown = f"![{alt_text}]({image_url})"

      image_start = text.find(markdown, current_index)
      if image_start == -1:
        continue

      if current_index < image_start:
        node_list.append(TextNode(text[current_index:image_start], TextType.TEXT))

      node_list.append(TextNode(alt_text, TextType.IMAGE, image_url))

      current_index = image_start + len(markdown)

    if current_index < len(text):
      node_list.append(TextNode(text[current_index:], TextType.TEXT))

  return node_list

def split_node_links(nodes: list[TextNode]):
  node_list = []
  
  for node in nodes:
    if node.text_type != TextType.TEXT:
      node_list.append(node)
      continue
    
    link_matches = extract_markdown_links(node.text)
    
    if not link_matches:
      node_list.append(node)
      continue
    
    text = node.text
    current_index = 0

    for link_text, link_url in link_matches:
      markdown = f"[{link_text}]({link_url})"

      link_start = text.find(markdown, current_index)
      if link_start == -1:
        continue  

      if current_index < link_start:
        node_list.append(TextNode(text[current_index:link_start], TextType.TEXT))

      node_list.append(TextNode(link_text, TextType.LINK, link_url))

      current_index = link_start + len(markdown)

    if current_index < len(text):
      node_list.append(TextNode(text[current_index:], TextType.TEXT))

  return node_list

def text_to_textnodes(txt):
  text_node = TextNode(txt, TextType.TEXT)
  node_list = split_nodes_delimiter([text_node], '**', TextType.BOLD)
  node_list = split_nodes_delimiter(node_list, '*', TextType.ITALIC)
  node_list = split_nodes_delimiter(node_list, "`", TextType.CODE)
  node_list = split_node_images(node_list)
  node_list = split_node_links(node_list)
  return node_list
