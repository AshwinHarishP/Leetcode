import java.util.Stack;
class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        int n = temperatures.length;
        int [] res = new int[n];
        Stack<Integer> st = new Stack();

        for(int i = 0; i < n; i++){
            while (!st.empty() && temperatures[st.peek()] < temperatures[i]){
                int ind = st.pop();
                res[ind] = i - ind;
            }
            st.push(i);
        }
        return res;
    }
}
