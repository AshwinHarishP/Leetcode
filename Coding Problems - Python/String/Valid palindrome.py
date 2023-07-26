class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ""
        for i in s:
            if i.isalnum() and i != " ":
                i = i.lower()
                new_str += i
        
        if new_str == " ":
            return True
        
        i = 0
        j = len(new_str) - 1

        for i in range(len(new_str)//2):
            if new_str[i] != new_str[j]:
                return False
            i += 1
            j -= 1
        return True
        
        
