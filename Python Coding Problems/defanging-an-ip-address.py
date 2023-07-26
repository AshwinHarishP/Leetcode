class Solution:
    def defangIPaddr(self, address: str) -> str:
        string = address.split(".")
        
        letters = ""
        for i in range(len(string)):
            letters +=  string[i] + "[.]"
        return(letters.strip("[.]"))
