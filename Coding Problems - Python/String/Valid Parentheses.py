class Solution:
    def isValid(self, s: str) -> bool:
        Stack = []
        dict_elements = {
            "[" : "]",
            "{" : "}",
            "(" : ")"
        }

        for i in s:
            if i in dict_elements.keys():
                Stack.append(i)
            else:
                if Stack == []:
                    return 0
                elif dict_elements[Stack[-1]] == i:
                    Stack.pop()
                else:
                    return 0
        
        if Stack == []:
            return 1
        else:
            return 0
