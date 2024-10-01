# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

pattern = r"(#[0-9a-fA-F]{6})|(#[0-9a-fA-F]{3})(?=[;),])"

if __name__ == "__main__":
    css_open = False
    css_statement = []
    for _ in range(int(input().rstrip())):
        css_statement.append(input())

    for statement in css_statement:
        if "{" in statement:
            css_open = True

        if "}" in statement:
            css_open = False

        if css_open:
            matches = re.finditer(pattern, statement)
            if matches:
                for match in matches:
                    print(match.group(0))