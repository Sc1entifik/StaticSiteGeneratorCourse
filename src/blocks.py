from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "p"
    HEADING = "h"
    CODE = "code"
    QUOTE = "blockquote"
    UNORDERED_LIST = "ul"
    ORDERED_LIST = "ol"

def markdown_to_blocks(markdown):
    return [block.strip() for block in markdown.split("\n\n") if block]   

def block_to_block_type(block):
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    elif block.startswith(("```\n")) and block.endswith(("```")):
        return BlockType.CODE
    elif all(line.startswith(">") for line in block.split("\n")):
        return BlockType.QUOTE
    elif all(line.startswith(f"- ") for line in block.split("\n")):
        return BlockType.UNORDERED_LIST
    elif all(line.startswith(f"{i}. ") for i, line in enumerate(block.split("\n"), start=1)): 
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH
