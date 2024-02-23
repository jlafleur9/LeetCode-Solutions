class Solution:
    def countPrimes(self, n: int) -> int:
        primes = 0
        
        if n == 0 or n == 1:
            return primes
        
        nonprimes = set()
        
        for num in range(2,n):
            if num not in nonprimes:
                primes += 1
                value = num + num
                nonprimes.add(value)
                while value < n:
                    value += num
                    nonprimes.add(value)
                continue
            #just skip even numbers 2 will always run through first if statement and add all even numbers will be added to nonprimes
            if num % 2 == 0:  
                continue
            if num in nonprimes:
                while value < n:
                    value += num
                    nonprimes.add(value)
        
        return primes
                
        