class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)

        if len(cost)<3:
            return sum(cost)
        mc=0
        for i in range(0,len(cost),3):
            if i+1<len(cost):
                mc+=(cost[i]+cost[i+1])
            else:
                mc+=(cost[i])
        return mc



