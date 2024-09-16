from typing import List

def get_bills(num_hunds: int, num_fifty: int, num_twenty: int, remainder: int) -> List[int]:
    print(f'Hunds: {num_hunds}, Fifties: {num_fifty}, Twenties: {num_twenty}, Remains: {remainder}')
    while remainder > 0:
        if num_fifty > 0:
            num_fifty = num_fifty - 1
            remainder = remainder + 50
            if divmod(remainder, 20)[1] == 0:
                num_twenty = num_twenty + divmod(remainder, 20)[0]
                remainder = divmod(remainder, 20)[1]
        else:
            if num_hunds > 0:
                num_hunds = num_hunds - 1
                remainder = remainder + 100
                num_fifty = divmod(remainder, 50)[0]
                remainder = divmod(remainder, 50)[1]
                print(f'In 100s Hunds: {num_hunds}, Fifties: {num_fifty}, Twenties: {num_twenty}, Remains: {remainder}')


    return [num_hunds, num_fifty, num_twenty]

def withdraw(amount: int) -> List[int]:
    """Returns smallest amount of bills possible"""

    # gets number of 100 dollar bills
    hunds_remainder = divmod(amount, 100)
    hunds = hunds_remainder[0]
    remainder = hunds_remainder[1]

    # gets number of 50 dollar bills
    fifty_remainder = divmod(remainder, 50)
    fifty = fifty_remainder[0]

    # gets number of 20 dollar bills
    twenty_remainder = divmod(fifty_remainder[1], 20)
    twenty = twenty_remainder[0]

    return get_bills(hunds, fifty, twenty, twenty_remainder[1])



print(withdraw(330))