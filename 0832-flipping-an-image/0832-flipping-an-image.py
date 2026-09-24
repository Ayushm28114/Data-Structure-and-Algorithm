class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        for i in range(len(image)):
            for j in range(len(image[0])):
                image[i][j]^=1
                    
            image[i].reverse()
        return image