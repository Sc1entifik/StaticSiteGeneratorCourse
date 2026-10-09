from textnode import TextNode, TextType
from split_nodes import split_nodes_delimiter, split_nodes_image, split_nodes_link

def text_to_textnodes(text):
    text_nodes = [TextNode(text, TextType.TEXT)]
    delimiters_and_text_types = [("**", TextType.BOLD), ("_", TextType.ITALIC), ("`", TextType.CODE)] 
    text_nodes = split_nodes_image(text_nodes)
    text_nodes = split_nodes_link(text_nodes)

    for delimiter, text_type in delimiters_and_text_types:
        text_nodes = split_nodes_delimiter(text_nodes, delimiter, text_type)

    return text_nodes
