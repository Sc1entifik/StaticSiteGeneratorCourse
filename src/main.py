from sync_static_to_public import sync_static_to_public
from generate_page import generate_pages_recursive
import sys

def main():
    source_path = "static"
    destination_path = "docs"
    basepath = "/" if len(sys.argv) == 1 else sys.argv[1]
    sync_static_to_public(source_path, destination_path)
    generate_pages_recursive(dir_path_content="content", template_path="template.html", dest_dir_path=destination_path, basepath=basepath)

main()
