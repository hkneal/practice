def calculate(years: int, base: float) -> int:
    for i in range(years):
        base += round(base * 0.013, 2)
        ot = base + round(base/2.0, 2)
        if (i+1) <= 1:
            print(f"After {i+1} year, the payrate would be ${round(base, 2)}, OT is: ${round(ot, 2):.2f} hourly")
        else:
            print(f"After {i+1} years, the payrate would be ${round(base, 2):.2f}, OT is: ${round(ot, 2):.2f} hourly")
    salary = round(base * 2080, 2)
    max_salary = round(salary + ( ot * 1040), 2)
    print(f"The Annual Salary is: ${salary:,.2f}, with max overtime, ${max_salary:,.2f}.")
    return round(base, 2)


print(f"${calculate(15, 23.53)}")