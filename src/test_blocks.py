import unittest
from markdown_to_blocks import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
    def test_common_use(self):
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
        print(f"Expected_Output: \n{expected_output}\n\nActual_Output:\n{markdown_to_blocks(markdown_string)}\n")
        self.assertEqual(markdown_to_blocks(markdown_string), expected_output)

    def test_extra_lines_between(self):
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


    def test_leading_and_trailing_lines(self):
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
