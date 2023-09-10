class Solution:
    def countBits(self, n: int) -> List[int]:
        lst=[]
        for x in range(0,n+1):
            if x>1:
                lst.append(lst[x//2]+(x%2))
            else:
                lst.append(x)
        return lst
