class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        count = Counter(tasks)  # get frequencies of variables ex. {X : 2, Y: 2}
        maxHeap = [-cnt for cnt in count.values()]  # build maxheap of frequencies using negated versions of nums
        heapq.heapify(maxHeap) #build heap
        time = 0
        q = collections.deque()

        while maxHeap or q:     # as long as there is at least 1 item/value in the maxHeap or queue
            time += 1           
            if maxHeap:
                cnt = heapq.heappop(maxHeap) + 1    #complete the max freq var task, and then add 1 to the count (1 closer to zero) so it reflects new frequency
                if cnt != 0:        # if there are still 1 or more of that variable remaining
                    q.append([cnt, time + n])       #append it to the q with its cnt and its cooldown time
                
            if q and q[0][1] == time:           #if atleast 1 item in the queue and we have reached the cooldown time
                heapq.heappush(maxHeap, q.popleft()[0])     #push the var into the heap, then repeat the loop till finished

        return time         
                