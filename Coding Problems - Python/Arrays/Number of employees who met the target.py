class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        count = 0
        #Traversing elemnts in list and comparing hours with target
        for i in hours:
            if i >= target:
                count += 1
        return count
