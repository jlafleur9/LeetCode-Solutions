class Solution:
    def countPrimes(self, n: int) -> int:
        primes = 0
        
        if n == 0 or n == 1 or n == 2:
            return primes
        
        nonprimes = set()
        
        if n == 3:
            primes += 1
            return primes
        
        #add 2 to primes and eliminate all even numbers. 
        if n > 3:
            primes += 1
            value = 4
            nonprimes.add(value)
            while value < n:
                value += 2
                nonprimes.add(value)
        
                
        
        
        for num in range(3,n):
            if num % 2 == 0:  
                continue
            if num not in nonprimes:
                primes += 1
                value = num * 3
                nonprimes.add(value)
                while value < n:
                    value += num * 2
                    nonprimes.add(value)
                continue
            if num in nonprimes:
                value = num * 3
                nonprimes.add(value)
                while value < n:
                    value += num * 2
                    nonprimes.add(value)
        
        return primes
                
        