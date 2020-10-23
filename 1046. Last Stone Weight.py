import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            heapq.heappush(heap, heapq.heappop(heap) - heapq.heappop(heap))
        return -heap[0]        
