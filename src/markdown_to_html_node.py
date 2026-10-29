from htmlnode import HTMLNode, LeafNode, ParentNode
from blocks import BlockType, markdown_to_blocks, block_to_block_type
from textnode import text_node_to_html_node
from text_to_textnodes import text_to_textnodes

def markdown_to_html_node(markdown: str) -> HTMLNode:
    text_to_children = lambda text: list(map(text_node_to_html_node, text_to_textnodes(text)))
    blocks = markdown_to_blocks(markdown)
    blocks_and_block_types = [(block, block_to_block_type(block)) for block in blocks]
    html_nodes = [ParentNode(block_type, block) for block, block_type in blocks_and_block_types]
