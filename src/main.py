import textnode
from sync_static_to_public import sync_static_to_public
from generate_page import generate_page


def main():
    txtnode = textnode.TextNode("This is test text", textnode.TextType.TEXT, "www.test.com")
    print(txtnode)
    source_path = "static"
    destination_path = "public"
    sync_static_to_public(source_path, destination_path)
    generate_page("content/index.md", "template.html", "public/index.html")

main()
