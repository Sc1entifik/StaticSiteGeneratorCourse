import unittest
from split_nodes_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType

class TestSplitNodesDelimiter(unittest.TestCase):
    def test_bold_delimiter(self):
        text = "This **is bold** text __not this italic__ text or `this = 'code'` text."
        delimiter = "**"
        text_node = TextNode(text, TextType.TEXT)
        expected_result = [TextNode("This ", TextType.TEXT), TextNode("is bold", TextType.BOLD), TextNode(" text __not this italic__ text or `this = 'code'` text.", TextType.TEXT)]

        self.assertEqual(split_nodes_delimiter([text_node], delimiter, TextType.BOLD), expected_result)
