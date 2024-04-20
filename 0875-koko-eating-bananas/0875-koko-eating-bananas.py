class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minRate = 1
        maxRate = max(piles)
        result = maxRate
        
        while minRate <= maxRate:
            k = (minRate + maxRate) // 2
            hours = 0
            for bananas in piles:
                hours += math.ceil(bananas / k)
            
            if hours > h:
                minRate = k + 1
            else:
                maxRate = k - 1
                result = min(k, result)
                
        return result
                