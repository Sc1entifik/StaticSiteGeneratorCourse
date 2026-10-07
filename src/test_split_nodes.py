import unittest
from split_nodes import split_nodes_delimiter
from textnode import TextNode, TextType

class TestSplitNodes(unittest.TestCase):
    def test_bold_delimiter(self):
        text = "This **is bold** text __not this italic__ text or `this = 'code'` text."
        delimiter = "**"
        text_node = TextNode(text, TextType.TEXT)
        expected_result = [TextNode("This ", TextType.TEXT), TextNode("is bold", TextType.BOLD), TextNode(" text __not this italic__ text or `this = 'code'` text.", TextType.TEXT)]

        self.assertEqual(split_nodes_delimiter([text_node], delimiter, TextType.BOLD), expected_result)

    def test_italic_delimiter(self):
        text = "This **is bold** text __not this italic__ text or `this = 'code'` text."
        delimiter = "**"
        text_node = TextNode(text, TextType.TEXT)
        split_nodes = split_nodes_delimiter([text_node], delimiter, TextType.BOLD)
        delimiter = "__"
        expected_result = [TextNode("This ", TextType.TEXT), TextNode("is bold", TextType.BOLD), TextNode(" text ", TextType.TEXT), TextNode("not this italic", TextType.ITALIC), TextNode(" text or `this = 'code'` text.", TextType.TEXT)]

        self.assertEqual(split_nodes_delimiter(split_nodes, delimiter, TextType.ITALIC), expected_result)

    def test_code_delimiter(self):
        text = "This **is bold** text __not this italic__ text or `this = 'code'` text."
        delimiter = "**"
        text_node = TextNode(text, TextType.TEXT)
        split_nodes = split_nodes_delimiter([text_node], delimiter, TextType.BOLD)
        delimiter = "__"
        split_nodes = split_nodes_delimiter(split_nodes, delimiter, TextType.ITALIC)
        delimiter = "`"
        expected_result = [TextNode("This ", TextType.TEXT), TextNode("is bold", TextType.BOLD), TextNode(" text ", TextType.TEXT), TextNode("not this italic", TextType.ITALIC), TextNode(" text or ", TextType.TEXT), TextNode("this = 'code'", TextType.CODE),TextNode(" text.", TextType.TEXT)]


        self.assertEqual(split_nodes_delimiter(split_nodes, delimiter, TextType.CODE), expected_result)
