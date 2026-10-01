
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

        return "" if not kv_pairs else " ".join((f'{key}="{value}"' for key, value in kv_pairs))

    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"
