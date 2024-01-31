import java.util.Stack;
class Solution {
    public int evalRPN(String[] tokens) {
        ArrayList<Integer> Q = new ArrayList<>();
        Stack<String> st = new Stack();
        HashSet<String> op = new HashSet<>();
        op.add("+");
        op.add("-");
        op.add("*");
        op.add("/");

        for(String i: tokens){
            if(!op.contains(i)) Q.add(Integer.parseInt(i));
            
            else st.push(i);
            

            while(!st.empty() && Q.size() > 1){
                String operator = st.pop();
                int res = 0;
                if (operator.equals("+")) res = Q.get(Q.size() - 2) + Q.get(Q.size() - 1);
                

                else if (operator.equals("-")) res = Q.get(Q.size() - 2) - Q.get(Q.size() - 1);
                
                
                else if (operator.equals("*")) res = Q.get(Q.size() - 2) * Q.get(Q.size() - 1);
                
                else res = Q.get(Q.size() - 2) / Q.get(Q.size() - 1);
                
                
                Q.remove(Q.size() - 1);
                Q.remove(Q.size() - 1);
                Q.add(res);
            }
        }
        return Q.get(0);
    }
}
