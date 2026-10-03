from enum import Enum

from htmlnode import LeafNode

class TextType(Enum):
    PLAIN_TEXT = "plain text"
    BOLD_TEXT = "bold text"
    ITALIC_TEXT = "italic text"
    CODE_TEXT = "code text"
    LINK_TEXT = "link text"
    IMAGE_LINK = "image"


class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, text_node):
        if self.text != text_node.text or self.text_type != text_node.text_type or self.url != text_node.url:
            return False

        return True

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

def text_node_to_html_node(textnode):
    match textnode.text_type:
        case TextType.PLAIN_TEXT:
            return LeafNode(tag=None, value=textnode.text, props=None)
        
        case TextType.BOLD_TEXT:
            return LeafNode(tag="b", value=textnode.text, props=None)

        case TextType.ITALIC_TEXT:
            return LeafNode(tag="i", value=textnode.text, props=None)

        case TextType.CODE_TEXT:
            return LeafNode(tag="code", value=textnode.text, props=None)

        case TextType.LINK_TEXT:
            return LeafNode(tag="a", value=textnode.text, props={"href": textnode.url})

        case TextType.IMAGE_LINK:
            return LeafNode(tag="img", value="", props={"src":textnode.url, "alt":textnode.text})

        case _:
            raise Exception()
