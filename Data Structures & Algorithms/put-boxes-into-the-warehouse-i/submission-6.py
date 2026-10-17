class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        
        i = 0
        for boxHeight in sorted(boxes, reverse=True):
            if i < len(warehouse) and boxHeight <= warehouse[i]:
                i += 1
        
        return i




        