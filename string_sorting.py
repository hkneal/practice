# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
    s = input().rstrip()
    numseven, numsodd, uppers, lowers = [], [], [], []
    for ch in s:
        if ch.isnumeric():
            numseven.append(str(ch)) if int(ch) % 2 ==0 else numsodd.append(str(ch))
        elif ch.isupper():
            uppers.append(ch)
        else:
            lowers.append(ch)
    print("".join(sorted(lowers)) + "".join(sorted(uppers)) + "".join(sorted(numsodd)) + "".join(sorted(numseven)))