import random
class RandomizedSet:

    def __init__(self):
        self.rset = set()


    def insert(self, val: int) -> bool:
        if not val in self.rset:
             self.rset.add(val)
             return True
        else:
            return False


    def remove(self, val: int) -> bool:
        if val in self.rset:
            self.rset.remove(val)
            return True
        else:
            return False


    def getRandom(self) -> int:
        return random.choice(list(self.rset))

randomizedSet = RandomizedSet()
randomizedSet.insert(1); #Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); #Returns false as 2 does not exist in the set.
randomizedSet.insert(2); #Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); #getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); #Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); #2 was already in the set, so return false.
randomizedSet.getRandom(); #Since 2 is the only number in the set, getRandom() will always return 2.