import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        tag = "p"
        value = "This is the p text"
        children = None
        props = {"href":"https://test.com", "p":"another p text", "div":"I'm a div!"}
        node = HTMLNode(tag, value, children, props)
        props_string = f' href="{props.get("href")}" p="{props.get("p")}" div="{props.get("div")}"'
        self.assertEqual(node.props_to_html(), props_string)

    def test_to_html(self):
        tag = "p"
        value = "This is the p text"
        children = None
        props = {"href":"https://test.com", "p":"another p text", "div":"I'm a div!"}
        node = HTMLNode(tag, value, children, props)
        self.assertRaises(NotImplementedError, node.to_html)

    def test_html_node_print(self):
        tag = "p"
        value = "This is the p text"
        children = None
        props = {"href":"https://test.com", "p":"another p text", "div":"I'm a div!"}
        node = HTMLNode(tag, value, children, props)
        html_string = f"HTMLNode(tag={tag}, value={value}, children={children}, props={props})"
        self.assertEqual(repr(node), html_string)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        
    def test_leaf_to_html_div(self):
        node = LeafNode("div", "Hello, world!")
        self.assertEqual(node.to_html(), "<div>Hello, world!</div>")

    def test_leaf_repr(self):
        node = LeafNode("p", "Hello, world!")
        test_string = "LeafNode(tag=p, value=Hello, world!, props=None)"
        self.assertEqual(repr(node), test_string)



if __name__ == "__main__":
    unittest.main()
