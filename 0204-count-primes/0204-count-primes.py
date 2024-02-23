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
                nonprimes.update(range(num*3,n,num*2))
                
        
        return primes
                
        