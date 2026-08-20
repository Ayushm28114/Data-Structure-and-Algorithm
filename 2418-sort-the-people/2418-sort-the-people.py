class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        combined= zip(heights,names)
        sort= sorted(combined)
        dc=dict(sort)

        a=[]
        for key, value in dc.items():
            a.append(value)
        a=a[::-1]
        return a