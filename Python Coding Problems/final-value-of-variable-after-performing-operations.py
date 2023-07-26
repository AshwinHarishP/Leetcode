class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        # Traversing through list
        for i in range(len(operations)):
            # Case1: X increments by 1
            if operations[i] == "--X" or operations[i] == "X--":
                x -= 1
            #Case 2: X decrements by 1
            else:
                x += 1
        return x
