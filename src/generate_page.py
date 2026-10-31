import os
from markdown_to_html_node import markdown_to_html_node
from extract_title import extract_title

def generate_page(from_path: str, template_path: str, dest_path: str ):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    with open(from_path, "r") as md_object:
        md_string = md_object.read()

    with open(template_path, "r") as template_object:
        template_string = template_object.read()

    html_node = markdown_to_html_node(md_string)
    html_string = html_node.to_html()
    title = extract_title(md_string)
    template_string = template_string.replace("{{ Title }}", title)
    template_string = template_string.replace("{{ Content }}", html_string)

    if not os.path.exists(os.path.dirname(dest_path)):
        os.makedirs(os.path.dirname(dest_path))

    with open(dest_path, "w") as index_file:
        index_file.write(template_string)

