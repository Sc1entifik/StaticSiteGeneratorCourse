def extract_title(markdown: str) -> str : 
    markdown_lines = markdown.split("\n")

    for line in markdown_lines:
        if len(line) >= 2:
            if line[0:2] == "# ":
                return line[2:].strip()

    return "H1 element not found!"
