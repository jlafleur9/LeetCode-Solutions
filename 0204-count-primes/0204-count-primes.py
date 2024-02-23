class Solution:
    def countPrimes(self, n: int) -> int:
        primes = 0
        
        if n < 3:
            return primes
        
        primes += 1
        nonprimes = set()
        
        for num in range(3,n,2):
            if num not in nonprimes:
                primes += 1
                value = num * 3
                while value < n:
                    nonprimes.add(value)
                    value += num * 2
                
        
        return primes
                
        