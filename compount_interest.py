def compound_interest(principal: float, rate: int, contribution: float, years: int) -> float:
    total = principal
    rate = rate / 100

    for _ in range(years):
        total = total + (total * rate) + contribution

    return round(total, 2)

print(f'{compound_interest(500, 10, 50, 3):.2f}')