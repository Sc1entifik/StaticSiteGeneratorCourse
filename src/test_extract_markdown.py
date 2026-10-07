import unittest
from extract_markdown import extract_markdown_images, extract_markdown_links

class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links("This is my [webpage!](https://www.example.com)")
        self.assertListEqual([("webpage!", "https://www.example.com")], matches)

    def test_extract_markdown_links_does_not_match_images(self):
        matches = extract_markdown_links(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([], matches)

    def test_extract_markdown_images_matches_multiple(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) here is another image ![image2](https://notrealimage.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png"), ("image2", "https://notrealimage.png")], matches)

    def test_extract_markdown_links_matches_multiple(self):
        matches = extract_markdown_links(
            "This is text with an [webpage](https://i.imgur.com/zjjcJKZ.com) here is another page [webpage2](https://notrealwebpage.com)"
        )
        self.assertListEqual([("webpage", "https://i.imgur.com/zjjcJKZ.com"), ("webpage2", "https://notrealwebpage.com")], matches)

    def test_extract_markdown_images_unused_tags(self):
        matches = extract_markdown_images(
            "This is text with an ![](https://i.imgur.com/zjjcJKZ.com) here is another page ![](https://notrealwebpage.com)"
        )
        self.assertListEqual([("", "https://i.imgur.com/zjjcJKZ.com"), ("", "https://notrealwebpage.com")], matches)

    def test_extract_markdown_links_unused_tags(self):
        matches = extract_markdown_links(
            "This is text with an [](https://i.imgur.com/zjjcJKZ.com) here is another page [](https://notrealwebpage.com)"
        )
        self.assertListEqual([("", "https://i.imgur.com/zjjcJKZ.com"), ("", "https://notrealwebpage.com")], matches)

