import unittest
from text_to_textnodes import text_to_textnodes
from textnode import TextNode, TextType


class TestTextToTextNodes(unittest.TestCase):
    def test_common_target(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        expected_output = [
        TextNode("This is ", TextType.TEXT),
        TextNode("text", TextType.BOLD),
        TextNode(" with an ", TextType.TEXT),
        TextNode("italic", TextType.ITALIC),
        TextNode(" word and a ", TextType.TEXT),
        TextNode("code block", TextType.CODE),
        TextNode(" and an ", TextType.TEXT),
        TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
        TextNode(" and a ", TextType.TEXT),
        TextNode("link", TextType.LINK, "https://boot.dev"),
        ]

        self.assertEqual(text_to_textnodes(text), expected_output)

    def test_combination_density(self):
        text = "Here is **bold**_italic_ texts."
        expected_output = [
            TextNode("Here is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode("italic", TextType.ITALIC),
            TextNode(" texts.", TextType.TEXT)
        ]

        self.assertEqual(text_to_textnodes(text), expected_output)

    def test_plain_text(self):
        text = "Here is some plain old text."
        expected_output = [TextNode("Here is some plain old text.", TextType.TEXT)]

        self.assertEqual(text_to_textnodes(text), expected_output)

    def test_only_syntax(self):
        text = "`test = 'This should pass'`"
        expected_output = [TextNode("test = 'This should pass'", TextType.CODE)]

        self.assertEqual(text_to_textnodes(text), expected_output)

    def test_empty_string(self):
        text = ""
        expected_output = []

        self.assertEqual(text_to_textnodes(text), expected_output)
