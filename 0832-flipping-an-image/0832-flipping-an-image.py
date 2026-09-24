class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        for i in range(len(image)):
            for j in range(len(image[0])):
                if image[i][j]==1:
                    image[i][j]=0
                else:
                    image[i][j]=1
                    
            image[i].reverse()
        return image