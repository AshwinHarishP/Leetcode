class Solution(object):
    def sortArrayByParity(self, nums):
        if len(nums) == 1:
            return nums
        else:
            even_list = []
            odd_list = []

            for i in nums:
                if i % 2 == 0:
                    even_list.append(i)
                    
                else:
                    odd_list.append(i)
                    
            even_list.extend(odd_list)
            
            return(even_list)
        
