from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        split_text = node.text.split(delimiter)

        if len(split_text) %2 == 0:
            raise Exception("Odd number of delimiters present!!")

        split_nodes = [TextNode(text, node.text_type) if index % 2 ==0 else TextNode(text, text_type) for index, text in enumerate(split_text)]
        new_nodes.extend(split_nodes)

    return new_nodes



