import operator
from operator import itemgetter
def person_lister(f):
    def inner(people):
        # complete the function
        people = sorted(people, key=lambda x: int(x[2]))
        # people = people.sort(key=itemgetter(2))
        return [f(p) for p in people]
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')


"['+91 '+num[-10:-5]+' '+num[-5:] for num in l]"