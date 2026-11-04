from textnode import TextNode, TextType
from extract_markdown import extract_markdown_images, extract_markdown_links

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        split_text = node.text.split(delimiter)

        if len(split_text) %2 == 0:
            raise Exception("Odd number of delimiters present!!")

        split_nodes = [TextNode(text, TextType.TEXT) if index % 2 == 0 else TextNode(text, text_type) for index, text in enumerate(split_text) if text]
        new_nodes.extend(split_nodes)

    return new_nodes

def _extraction_function(extraction_function):
    def decorator(old_nodes, text_type):
        new_nodes = []

        for node in old_nodes:
            if node.text_type != TextType.TEXT:
                new_nodes.append(node)
                continue

            remaining_text = node.text
            for extraction in extraction_function(node.text):
                delimiter = f"![{extraction[0]}]({extraction[1]})" if text_type == TextType.IMAGE else f"[{extraction[0]}]({extraction[1]})"
                before, remaining_text= remaining_text.split(delimiter, 1)
                split_nodes = [TextNode(extraction[0], text_type, extraction[1])] if not before else[TextNode(before, TextType.TEXT), TextNode(extraction[0], text_type, extraction[1])]
                new_nodes.extend(split_nodes)

            if remaining_text:
                new_nodes.append(TextNode(remaining_text, TextType.TEXT))

        return old_nodes if not new_nodes else new_nodes
    return decorator


def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    split_nodes_by_image = _extraction_function(extract_markdown_images)
    
    return split_nodes_by_image(old_nodes, TextType.IMAGE)

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    split_nodes_by_link = _extraction_function(extract_markdown_links)

    return split_nodes_by_link(old_nodes, TextType.LINK)
