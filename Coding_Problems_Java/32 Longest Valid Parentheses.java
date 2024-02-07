class Solution {
    public int longestValidParentheses(String s) {
        int max_len = 0;
        ArrayList<Integer> st = new ArrayList<>();
        st.add(-1);

        for(int i = 0; i < s.length(); i++){
            char ch = s.charAt(i);
            if (ch == '('){
                st.add(i);
            }
            else{
                st.remove(st.size()-1);
                if(st.isEmpty()){
                    st.add(i);
                }
                max_len = Math.max(max_len, i - st.get(st.size()-1));
            }
        }
        return max_len;
    }
}
