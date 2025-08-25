import inflect
counter = inflect.engine()

ONES_LETTER_COUNTS = {0: "", 1: "one", 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
TEENS_LETTER_COUNTS = {0: "", 10: "ten", 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
BY_TENS_COUNTS = {20: 'twenty', 30: "thirty", 40:"forty", 50:"fifty", 60:"sixty", 70:"seventy", 80:"eighty", 90:"ninety" }

def total_letters(n):
    sum = 0
    for i in range(1, n+1):
        if i < 10:
            sum += len(ONES_LETTER_COUNTS[i])
        elif i < 20:
            sum += len(TEENS_LETTER_COUNTS[i])
        elif i < 100:
            tens = (i // 10) * 10
            ones = i % 10
            sum += (len(BY_TENS_COUNTS[tens]) + len(ONES_LETTER_COUNTS[ones]))
        elif i < 1000:
            hundreds = (i // 100)
            num = i - (hundreds * 100)

            if num < 10 :
                sum += (len(ONES_LETTER_COUNTS[hundreds]) + len("hundredand") + len(ONES_LETTER_COUNTS[num]))
                if i == 100:
                    sum -= 3
            elif num < 20:
                sum += (len(ONES_LETTER_COUNTS[hundreds]) + len("hundredand") + len(TEENS_LETTER_COUNTS[num]))
            else:
                tens = (num // 10) * 10
                ones = num % 10
                sum += (len(ONES_LETTER_COUNTS[hundreds]) + len("hundredand") + len(BY_TENS_COUNTS[tens]) + len(ONES_LETTER_COUNTS[ones]))
        else:
            sum += len("onethousand")
    return sum

n = 120
print(total_letters(n))

# n = 1000
# print(total_letters(5))

# ONES_LETTER_COUNTS = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten'}

# for i in range(1, n+1):
#     TENS_LETTER_COUNTS[i] = counter.number_to_words(i)

# print(TENS_LETTER_COUNTS)