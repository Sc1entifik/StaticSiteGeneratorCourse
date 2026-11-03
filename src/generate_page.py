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

def generate_pages_recursive(dir_path_content: str, template_path: str, dest_dir_path: str):
    for item in os.listdir(dir_path_content):
        current_from_path = os.path.join(dir_path_content, item)
        current_dest_path = os.path.join(dest_dir_path, item)
        if os.path.isfile(item):
            generate_page(current_from_path, template_path, current_dest_path)

        else:
            generate_pages_recursive(current_from_path, template_path, current_dest_path)


