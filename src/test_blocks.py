import unittest
from blocks import markdown_to_blocks, BlockType, block_to_block_type

class TestBlocks(unittest.TestCase):
    def test_common_use_markdown_to_blocks(self):
        markdown_string = '''
# This is a heading

This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

- This is the first list item in a list block
- This is a list item
- This is another list item
'''
        expected_output = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and _italic_ words inside of it.",
            "- This is the first list item in a list block\n- This is a list item\n- This is another list item"
        ]
        self.assertEqual(markdown_to_blocks(markdown_string), expected_output)

    def test_extra_lines_between_markdown_to_blocks(self):
        markdown_string = '''
# This is a heading




This is a paragraph of text. It has some **bold** and _italic_ words inside of it.







- This is the first list item in a list block
- This is a list item
- This is another list item
'''
        expected_output = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and _italic_ words inside of it.",
            "- This is the first list item in a list block\n- This is a list item\n- This is another list item"
        ]

        self.assertEqual(markdown_to_blocks(markdown_string), expected_output)


    def test_leading_and_trailing_lines_markdown_to_blocks(self):
        markdown_string = '''




# This is a heading




This is a paragraph of text. It has some **bold** and _italic_ words inside of it.







- This is the first list item in a list block
- This is a list item
- This is another list item

'''
        expected_output = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and _italic_ words inside of it.",
            "- This is the first list item in a list block\n- This is a list item\n- This is another list item"
        ]

        self.assertEqual(markdown_to_blocks(markdown_string), expected_output)

    def test_heading_block_to_block_type(self):
        input = "# I am a heading!"
        input2 = "## I am a heading!"
        input3 = "### I am a heading!"
        input4 = "#### I am a heading!"
        input5 = "##### I am a heading!"
        input6 = "###### I am a heading!"
        
        for heading in (input, input2, input3, input4, input5, input6):
            self.assertEqual(block_to_block_type(heading), BlockType.HEADING)

    def test_code_block_to_block_type(self):
        input = """```\n
        var = 1
        var2 = 2
        return var + var2
        ```"""

        self.assertEqual(block_to_block_type(input), BlockType.CODE)

    def test_invalid_code_block_to_block_type(self):
        input = """```var = 1
        var2 = 2
        return var + var2
        ```"""

        self.assertEqual(block_to_block_type(input), BlockType.PARAGRAPH)
