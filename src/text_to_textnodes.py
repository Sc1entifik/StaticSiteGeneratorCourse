from textnode import TextNode, TextType
from split_nodes import split_nodes_delimiter, split_nodes_image, split_nodes_link

def text_to_textnodes(text):
    text_nodes = [TextNode(text, TextType.TEXT)]

    for text_type, delimiter in [(TextType.TEXT, ""), (TextType.BOLD, "**"), (TextType.ITALIC, "__"), (TextType.CODE, "``")]:
        text_nodes = split_nodes_delimiter(text_nodes, delimiter, text_type)

    text_nodes = split_nodes_image(text_nodes)
    text_nodes = split_nodes_link(text_nodes)

    return text_nodes
