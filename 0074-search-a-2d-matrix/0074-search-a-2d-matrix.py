class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,r=0,len(matrix)-1

        while l<=r:
            mid=l+(r-l)//2

            if matrix[mid][0]==target:
                return True
            
            elif matrix[mid][0]>target:
                r=mid-1
            
            else:
                l=mid+1
            

        i,j=0,len(matrix[r])-1

        while i<=j:
            mid=i+(j-i)//2

            if matrix[r][mid]==target:
                return True

            elif matrix[r][mid]>target:
                j=mid-1

            else:
                i=mid+1

        return False