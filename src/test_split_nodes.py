import unittest
from split_nodes import split_nodes_delimiter, split_nodes_image, split_nodes_link
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


    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a [webpage](https://i.imgur.com/zjjcJKZ.com) and another [second webpage](https://i.imgur.com/3elNhQu.com)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("webpage", TextType.LINK, "https://i.imgur.com/zjjcJKZ.com"),
                TextNode(" and another ", TextType.TEXT),
                TextNode("second webpage", TextType.LINK, "https://i.imgur.com/3elNhQu.com"),
            ],
            new_nodes,
        )

    def test_split_images_no_images(self):
        node = TextNode("This is a text **WITH NO** images present", TextType.TEXT)

        self.assertEqual([node], split_nodes_image([node]))

    def test_split_links_no_links(self):
        node = TextNode("This is a text **WITH NO** links present", TextType.TEXT)

        self.assertEqual([node], split_nodes_link([node]))

    def test_split_images_handles_first_match(self):
        node = TextNode("![image](not_real_image.png) The rest of this is just text!", TextType.TEXT)

        self.assertEqual([TextNode("image", TextType.IMAGE, "not_real_image.png"), TextNode(" The rest of this is just text!", TextType.TEXT)], split_nodes_image([node]))

    def test_split_links_handles_first_match(self):
        node = TextNode("[webpage](not_real_image.com) The rest of this is just text!", TextType.TEXT)

        self.assertEqual([TextNode("webpage", TextType.LINK, "not_real_image.com"), TextNode(" The rest of this is just text!", TextType.TEXT)], split_nodes_link([node]))

    def test_split_images_and_links_pass_through_non_text_text_node(self):
        node = TextNode("**I am a bold text**", TextType.BOLD)
        self.assertEqual([node], split_nodes_image([node]))
        self.assertEqual([node], split_nodes_link([node]))
