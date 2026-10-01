import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        tag="p"
        value="This is the p text"
        children=None
        props = {"href":"https://test.com", "p":"another p text", "div":"I'm a div!"}
        node = HTMLNode(tag, value, children, props)
        props_string = f'href="{props.get("href")}" p="{props.get("p")}" div="{props.get("div")}"'
        self.assertEqual(node.props_to_html(), props_string)





if __name__ == "__main__":
    unittest.main()
