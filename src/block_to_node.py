from htmlnode import ParentNode
from text_to_textnodes import text_to_textnodes
from textnode import TextType, TextNode, text_node_to_html_node
from blocks import BlockType, header_tag

def text_to_children(text):
    return list(map(text_node_to_html_node, text_to_textnodes(text)))

def heading_block_to_node(block):
    tag = header_tag(block)
    stripped_text = block.lstrip("#").lstrip()
    children = text_to_children(stripped_text)
    return ParentNode(tag=tag, children=children)

def quote_block_to_node(block):
    lines = block.split("\n")
    stripped_lines = [line.lstrip(">").strip() for line in lines]
    stripped_text = " ".join(stripped_lines)
    children = text_to_children(stripped_text)
    return ParentNode(tag=BlockType.QUOTE.value, children=children)

def paragraph_block_to_node(block):
    text = " ".join(block.split("\n"))
    children = text_to_children(text)
    return ParentNode(tag=BlockType.PARAGRAPH.value, children=children)

def code_block_to_node(block):
    code_block = block.strip("```").lstrip()
    node = text_node_to_html_node(TextNode(text=code_block, text_type=TextType.CODE))
    return ParentNode(tag="pre", children=[node])

def unordered_list_to_node(block):
    lines = block.split("\n")
    stripped_lines = (line.removeprefix("- ").strip() for line in lines)
    children = [ParentNode(tag="li", children=text_to_children(stripped_line)) for stripped_line in stripped_lines]
    return ParentNode(tag=BlockType.UNORDERED_LIST.value, children=children)

def ordered_list_to_node(block):
    lines = block.split("\n")
    stripped_lines = (line.removeprefix(f"{index + 1}. ").strip() for index, line in enumerate(lines))
    children = [ParentNode(tag="li", children=text_to_children(stripped_line)) for stripped_line in stripped_lines]
    return ParentNode(tag=BlockType.ORDERED_LIST.value, children=children)


def blocktype_to_node(blocktype):
    blocknode_dictionary = {BlockType.HEADING.value: heading_block_to_node, BlockType.QUOTE.value: quote_block_to_node, BlockType.PARAGRAPH.value: paragraph_block_to_node, BlockType.CODE.value: code_block_to_node, BlockType.UNORDERED_LIST.value: unordered_list_to_node, BlockType.ORDERED_LIST.value: ordered_list_to_node}
    return blocknode_dictionary.get(blocktype)
