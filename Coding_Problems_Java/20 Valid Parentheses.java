class Solution {
    public boolean isValid(String s) {
        HashMap<Character, Character> pDict = new HashMap<>();
        pDict.put('(', ')');
        pDict.put('{', '}');
        pDict.put('[', ']');

        Stack<Character> stack = new Stack<>();

        for (char element : s.toCharArray()) {
            if (pDict.containsKey(element)) {
                stack.push(element);
            } else {
                if (stack.isEmpty()) {
                    return false;
                } else {
                    if (element == pDict.get(stack.peek())) {
                        stack.pop();
                    } else {
                        return false;
                    }
                }
            }
        }

        return stack.isEmpty();
    }
}
