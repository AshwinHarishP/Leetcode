class Solution(object):
    def winnerOfGame(self, colors):
        """
        :type colors: str
        :rtype: bool
        """
        concA, concB, alice, bob = 0, 0, 0, 0

        for i in range(len(colors)):
            if colors[i] == "A":
                concA += 1
                concB = 0
            
                if concA >= 3:
                    concA = 2
                    alice += 1

            elif colors[i] == "B":
                concB += 1
                concA = 0
            
                if concB >= 3:
                    concB = 2
                    bob += 1
            
        return alice > bob
