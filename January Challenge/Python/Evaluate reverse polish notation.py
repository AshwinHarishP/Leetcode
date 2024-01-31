class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        Q = []
        st = []
        op = {"+","-","*","/"}

        for i in tokens:
            if i not in op:
                Q.append(int(i))
            else:
                st.append(i)

            while st and len(Q) > 1:
                operator = st.pop()
                if operator == "+":
                    res = int(Q.pop(-2)) + int(Q.pop(-1))

                elif operator == "-":
                    res = int(Q.pop(-2)) - int(Q.pop(-1))

                elif operator == "*":
                    res = int(Q.pop(-2)) * int(Q.pop(-1))
                
                else:
                    res = int((Q.pop(-2)) / (Q.pop(-1)))

                Q.append(res) 
        
        return Q.pop()
