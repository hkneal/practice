lst = '{}}'

OPEN_BRACKETS = ["(", "[", "{"]

def bracket_check(s: str) -> bool:
    stack = []

    for c in s:
        if c in OPEN_BRACKETS:
            stack.append(c)
        else:
            match(c):
                
                case ")":
                    if len(stack) > 0 and stack[-1] == "(":
                        stack.pop()
                    else:
                        return False

                case "]":
                    if len(stack) > 0 and stack[-1] == "[":
                        stack.pop()
                    else:
                        return False

                case "}":
                    if len(stack) > 0 and stack[-1] == "{":
                        stack.pop()
                    else:
                        return False

    if len(stack) == 0:
        return True
            
    return False

print(bracket_check(lst))