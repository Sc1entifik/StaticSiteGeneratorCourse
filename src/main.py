import textnode


def main():
    txtnode = textnode.TextNode("This is test text", textnode.TextType.PLAIN_TEXT, "www.test.com")
    print(txtnode)

main()
