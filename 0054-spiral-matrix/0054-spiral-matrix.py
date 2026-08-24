class Solution:
    def spiralOrder(self, m: List[List[int]]) -> List[int]:
        top, bottom = 0, len(m)-1
        left, right = 0, len(m[0])-1
        result = []

        while top<=bottom and left<=right:

            for a in range(left, right+1):
                result.append(m[top][a])
            top+=1

            for b in range(top, bottom+1):
                result.append(m[b][right])
            right-=1

            if top<=bottom:
                for c in range(right, left-1, -1):
                    result.append(m[bottom][c])
                bottom-=1

            if left<=right:
                for d in range(bottom, top-1, -1):
                    result.append(m[d][left])
                left+=1

        return result