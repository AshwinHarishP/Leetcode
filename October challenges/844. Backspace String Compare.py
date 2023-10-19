class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_1 = []
        stack_2 = []
        for i in s:
            if i != "#":
                stack_1.append(i)
            elif stack_1:
                stack_1.pop()

        for i in t:
            if i != "#":
                stack_2.append(i)
            elif stack_2:
                stack_2.pop()

        if stack_1 == stack_2:
            return True
        return False
        
