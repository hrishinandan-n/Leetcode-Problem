1class Solution:
2    def lastStoneWeight(self, stones: List[int]) -> int:
3        stones = [-stone for stone in stones]
4        heapq.heapify(stones)
5        
6        while len(stones) > 1:
7            y = -heapq.heappop(stones)  # largest
8            x = -heapq.heappop(stones)  # second largest
9            
10            if y != x:
11                heapq.heappush(stones, -(y - x))
12        
13        return -stones[0] if stones else 0