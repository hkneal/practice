class Solution:
    def reverse(self, x: int) -> int:
        set_neg = False
        if x < 0:
            set_neg = True
            x = str(x).replace("-", "")
        else:
            x = str(x)
        x_list = reversed(list((x)))
        x_list = "".join(x_list)
        # print(x_list)
        if set_neg:
            x_list = "-" + x_list
        x_list = int(x_list)
        if x_list < -2147483648 or x_list > 2147483647:
            return 0
        else:
            return x_list


print(Solution().reverse(123))