class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:

        def isPrime(n):
            if n<2:
                return False
            for i in range(2,int(n**0.5)+1):
                if n%i==0:
                    return False
            return True

        c=0
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        
        for i in range(left, right+1):
            count=0
            m=i
            while m > 0:
                if m & 1:
                    count+=1
                m>>=1
            if count in primes:
                c+=1
        return c