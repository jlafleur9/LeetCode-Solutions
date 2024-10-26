class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
    
        # Step 2: Use a heap to find the k most frequent elements
        # The heap will store tuples in the form (frequency, element)
        # We use a min-heap of size k, so we can pop the smallest item if the heap grows beyond k
        heap = []
        for num, freq in count.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)

        # Step 3: Extract the elements from the heap
        return [num for freq, num in heap]
        
        
        
        
#         count = {}
        
#         for num in nums:
#             count[num] = 1 + count.get(num, 0)
            
#         frequency = [[] for i in range(len(nums) + 1)]
        
#         for num, c in count.items():
#             frequency[c].append(num)
        
#         result = []
        
#         for index in range(len(frequency) -1, 0, -1):
#             for num in frequency[index]:
#                 result.append(num)
#                 if len(result) == k:
#                     return result

