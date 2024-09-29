# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
import email.utils
pattern = r"^[a-zA-Z][\w.\-_]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$"

def validate_email(email: str) -> bool:
    return bool(re.match(pattern, email))

def validate_name(name: str) -> bool:
    # print(name)
    return name[0].isalpha()

if __name__ == "__main__":
    for _ in range(int(input().rstrip())):
        name, email_str = input().split()
        parsed_email_str = email.utils.parseaddr(email_str)
        # email_str = email.utils.parseaddr(str)
        if validate_email(parsed_email_str[-1]) and validate_name(name):
            print(name, email_str)

"""
7
dheeraj <dheeraj-234@gmail.com>
crap <itsallcrap>
harsh <harsh_1234@rediff.in>
kumal <kunal_shin@iop.az>
mattp <matt23@@india.in>
harsh <.harsh_1234@rediff.in>
harsh <-harsh_1234@rediff.in>
"""

"""
dheeraj <dheeraj-234@gmail.com>
harsh <harsh_1234@rediff.in>
kumal <kunal_shin@iop.az>
"""