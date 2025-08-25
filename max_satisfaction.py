def max_satisfaction(exp, cards):
    print(exp, cards)
    exp.sort()
    cards.sort()
    met_expectations = 0

    exp_num = 0
    card_num = 0
    max_loops = min(len(exp), len(cards))

    while card_num < max_loops:
        # print(f"Cardno: {card_num}, Length: {len(cards)}")
        if cards[card_num] >= exp[exp_num]:
            met_expectations += 1
            card_num += 1
            exp_num += 1
        else:
            card_num += 1


    return met_expectations

Expectations = [7, 5, 3]
Cards = [10, 12, 11, 20, 50, 20]
print(max_satisfaction(Expectations, Cards))