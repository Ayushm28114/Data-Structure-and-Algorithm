class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxm = max(candies)
        result=[]

        for num in candies:
            a=num + extraCandies
            if a>=maxm:
                result.append(True)
            else:
                result.append(False)

        return result