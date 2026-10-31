from sync_static_to_public import sync_static_to_public
from generate_page import generate_page


def main():
    source_path = "static"
    destination_path = "public"
    sync_static_to_public(source_path, destination_path)
    generate_page(from_path="content/index.md", template_path="template.html", dest_path="public/index.html")

main()
