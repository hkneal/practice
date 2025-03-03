from typing import List

def numRescueBoats(people: List[int], limit: int) -> int:
    num_boats = 0
    people.sort()
    heaviest = len(people) -1
    lightest = 0
    while heaviest >= lightest:
        if people[heaviest] + people[lightest] <= limit:
            heaviest -= 1
            lightest += 1
        else:
            heaviest -=1
        num_boats +=1

    return num_boats


people = [3,2,2,1]
limit = 3
print(numRescueBoats(people, limit))