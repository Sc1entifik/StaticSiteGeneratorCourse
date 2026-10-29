from htmlnode import ParentNode
from blocks import BlockType, header_tag, markdown_to_blocks, block_to_block_type
from textnode import TextNode, text_node_to_html_node
from text_to_textnodes import text_to_textnodes

def markdown_to_html_node(markdown: str) -> ParentNode:
    text_to_children = lambda text: list(map(text_node_to_html_node, text_to_textnodes(text)))
    handle_code_block = lambda text, text_type: ParentNode("pre", text_node_to_html_node(TextNode(text, text_type))) 
    blocks = markdown_to_blocks(markdown)
    blocks_and_block_types = (
        (block, header_tag(block) if (block_type := block_to_block_type(block)) == BlockType.HEADING else block_type.value)
        for block in blocks
    )
    html_nodes = [ParentNode(tag=block_type, children=text_to_children(block)) if block_type != BlockType.CODE else handle_code_block(text=block, text_type=block_type) for block, block_type in blocks_and_block_types]

    return ParentNode(tag="div", children=html_nodes)
