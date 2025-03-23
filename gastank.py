from typing import List
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        if sum(gas) < sum(cost):
            return -1

        gas_tank = 0
        starting_index = 0

        for i in range(len(gas)):
            gas_tank += (gas[i] - cost[i])
            if gas_tank < 0:
                gas_tank = 0
                starting_index = i + 1


        return starting_index

    # def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

    #     if sum(gas) < sum(cost):
    #         return -1

    #     gas_tank = 0
    #     total_gas = 0
    #     starting_index = 0

    #     for i in range(len(gas)):
    #         current = gas[i] - cost[i]
    #         total_gas += current
    #         gas_tank += current

    #         if gas_tank < 0:
    #             starting_index = i + 1
    #             gas_tank = 0

    #     if gas_tank >= 0:
    #         return starting_index
    #     return -1


gas = [5,1,2,3,4]
cost = [4,4,1,5,1]

print(Solution().canCompleteCircuit(gas, cost))