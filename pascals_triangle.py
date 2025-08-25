from typing import List
def generate(numRows: int) -> List[int]:
    if numRows <= 0:
        return []

    triange = []
    for i in range(numRows):
        if i == 0:
            triange.append([1])
        else:
            add_lst = [1]

            if i >= 2:
                for j in range(1, i):
                    add_lst.append(triange[i-1][j-1] + triange[i-1][j])
            add_lst.append(1)
            triange.append(add_lst)
    return triange

numRows = 4
print(generate(numRows))
