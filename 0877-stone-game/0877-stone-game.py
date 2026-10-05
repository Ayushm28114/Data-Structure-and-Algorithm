class Solution:
    def stoneGame(self, piles: list[int]) -> bool:
        alice, bob = 0, 0
        s, e = 0, len(piles)-1
        turn=0   # '0' for Alice and '1' for Bob

        while s<=e:
            if turn==0:
                if piles[s]>piles[e]:
                    alice+=piles[s]
                    s+=1
                else:
                    alice+=piles[e]
                    e-=1
            else:
                if piles[s]>=piles[e]:
                    bob+=piles[s]
                    s+=1
                else:
                    bob+=piles[e]
                    e-=1
        return alice>bob