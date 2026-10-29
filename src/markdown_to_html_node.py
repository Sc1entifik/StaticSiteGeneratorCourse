from htmlnode import HTMLNode, LeafNode, ParentNode
from blocks import BlockType, markdown_to_blocks, block_to_block_type

def markdown_to_html_node(markdown: str) -> HTMLNode:
    blocks = markdown_to_blocks(markdown)
    blocks_and_block_types = [(block, block_to_block_type(block)) for block in blocks]
