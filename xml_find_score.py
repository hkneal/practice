import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    # your code goes here
    sum = len(node.attrib)
    entries = node.findall('entry')

    for entry in entries:
        for child in entry:
            sum += len(child.attrib)

    for child in node:
        sum += len(child.attrib)

    return sum


if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))