class Solution:
    def isPalindrome(self, x: int) -> bool:
        string = str(x)

        i = 0  # Traversing from first
        j = len(string) -1  # Traversing from last 

        # Checking element from first and last

        for i in range(len(string)//2):
            if string[i] != string[j]:
                return False    # Not matched
            i += 1
            j -= 1

        return True    # If matched 
