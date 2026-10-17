class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:


        stones.sort()

        curr = stones.pop() - stones.pop()

        if curr > 0:
            stones.append(curr)

        return stones[0] if stones else 0


        