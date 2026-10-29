from htmlnode import ParentNode
from blocks import BlockType, header_tag, markdown_to_blocks, block_to_block_type
from block_to_node import blocktype_to_node

def markdown_to_html_node(markdown: str) -> ParentNode:
    blocks = markdown_to_blocks(markdown)
    blocks_and_block_types = (
        (block, header_tag(block) if (block_type := block_to_block_type(block)) == BlockType.HEADING else block_type.value)
        for block in blocks
    )
    html_nodes = [blocktype_to_node(block_type)(block) for block, block_type in blocks_and_block_types]

    return ParentNode(tag="div", children=html_nodes)
