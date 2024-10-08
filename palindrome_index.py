def palindromeIndex(s):
    # Write your code here
    list_s = list(s)
    l = len(s)

    if list_s == list(reversed(list_s)):
        return -1

    for i in range(len(s)//2):

        if s[i] != s[l-1-i]:
            list_s = list(s)
            list_s.pop(i)
            rev_lst = list(reversed(list_s))
            if list_s == rev_lst:
                return(i)

            else:
                list_s = list(s)
                list_s.pop(l-1-i)
                rev_lst = list(reversed(list_s))
                if list_s == rev_lst:
                    return(l-1-i)
            return -1

    return -1


print(palindromeIndex("baab"))