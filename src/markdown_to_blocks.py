from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown):
    return [block.strip() for block in markdown.split("\n\n") if block]   

def block_to_block_type(block):
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    elif block.startswith(("```\n")) and block.endswith(("```")):
        return BlockType.CODE
    elif all(line.startswith(">") for line in block.strip("\n")):
        return BlockType.QUOTE
    elif all(line.startswith(f"- ") for line in block.strip("\n")):
        return BlockType.UNORDERED_LIST
    elif all(line.startswith(f"{i}. ") for i, line in enumerate(block.strip("\n"), start=1)): 
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH
