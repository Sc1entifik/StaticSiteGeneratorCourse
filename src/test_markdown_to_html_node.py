import unittest
from markdown_to_html_node import markdown_to_html_node

class TestMarkdownToHtmlNode(unittest.TestCase):
    def test_paragraphs(self):
        md = """
    This is **bolded** paragraph\ntext in a p\ntag here

    This is another paragraph with _italic_ text and `code` here

    """

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that __should__ remain
the **same** even with inline stuff
```
"""
        assertion = "<div><pre><code>This is text that __should__ remain\nthe **same** even with inline stuff\n</code></pre></div>"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(html, assertion)

    def test_heading_block(self):
        md = "# I AM A HEADER!!!"
        node = markdown_to_html_node(md)
        html = node.to_html()
        assertion = "<div><h1>I AM A HEADER!!!</h1></div>"
        self.assertEqual(html, assertion)

        md = "## I AM A HEADER!!!"
        node = markdown_to_html_node(md)
        html = node.to_html()
        assertion = "<div><h2>I AM A HEADER!!!</h2></div>"
        self.assertEqual(html, assertion)

        md = "### I AM A HEADER!!!"
        node = markdown_to_html_node(md)
        html = node.to_html()
        assertion = "<div><h3>I AM A HEADER!!!</h3></div>"
        self.assertEqual(html, assertion)

        md = "#### I AM A HEADER!!!"
        node = markdown_to_html_node(md)
        html = node.to_html()
        assertion = "<div><h4>I AM A HEADER!!!</h4></div>"
        self.assertEqual(html, assertion)

        md = "##### I AM A HEADER!!!"
        node = markdown_to_html_node(md)
        html = node.to_html()
        assertion = "<div><h5>I AM A HEADER!!!</h5></div>"
        self.assertEqual(html, assertion)

        md = "###### I AM A HEADER!!!"
        node = markdown_to_html_node(md)
        html = node.to_html()
        assertion = "<div><h6>I AM A HEADER!!!</h6></div>"
        self.assertEqual(html, assertion)
