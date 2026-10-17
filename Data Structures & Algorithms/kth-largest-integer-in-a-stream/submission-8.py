class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = nums
        self.k = k
        Heapq.heapify(nums)
        while len(nums) > 1:
            heapq.heappop(nums)
        
        

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > 1:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
        
