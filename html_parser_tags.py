from html.parser import HTMLParser

class my_HTLM_Parser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print(tag)
        if attrs:
            for attr in attrs:
                print("->", attr[0], ">", attr[1])

    # def handle_endtag(self, tag):
    #     print("End   :", tag)

    def handle_startendtag(self, tag, attrs):
        print(tag)
        if attrs:
            for attr in attrs:
                print("->", attr[0], ">", attr[1])

if __name__ == "__main__":
    parser = my_HTLM_Parser()
    for _ in range(int(input())):
        parser.feed(input())