class HTMLNode():

    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        
    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        kv_pairs = None if not self.props else self.props.items()
        injection_string = lambda x: f" {x}"

        return "" if not kv_pairs else injection_string(" ".join((f'{key}="{value}"' for key, value in kv_pairs)))

    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if not self.value:
            raise ValueError()

        elif not self.tag:
            return self.value

        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode(tag={self.tag}, value={self.value}, props={self.props})"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if not self.tag:
            raise ValueError()

        elif not self.children:
            raise ValueError("Children node required but not found.")

        else:
            child_node_html = "".join(map(lambda x: x.to_html(), self.children))
            return f"<{self.tag}{self.props_to_html()}>{child_node_html}</{self.tag}>"
