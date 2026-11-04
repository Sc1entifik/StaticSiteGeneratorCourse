import unittest
from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_extract_title_easy(self):
        md = "# I AM A HEADER!!!!"
        title = extract_title(md)
        self.assertEqual(title, "I AM A HEADER!!!!")

    def test_extract_title_multiple(self):
        md = "# I AM THE HEADER!!!!\nThis is some boring text that comes under the header yada yada\n## I AM SUBHEDER 1!!!!!"
        title = extract_title(md)
        self.assertEqual(title, "I AM THE HEADER!!!!")

    def test_only_extracts_first_main_header(self):
        md = "# I AM THE HEADER!!!!\nMore boring text nobody cares about!!!!\n# I AM A POORLY WRITTEN FALSE MAIN HEADER WHICH SHOULD NOT BE USED!"
        title = extract_title(md)
        self.assertEqual(title, "I AM THE HEADER!!!!")

    def test_strips_whitespace(self):
        md = "# I AM THE HEADER!!!!  \nEven more boring text even though there is tricky whitespace to get rid of."
        title = extract_title(md)
        self.assertEqual(title, "I AM THE HEADER!!!!")
