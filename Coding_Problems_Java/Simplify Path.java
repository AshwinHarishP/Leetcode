import java.util.Stack;
class Solution {
    public String simplifyPath(String path) {
        String [] s = path.split("/");
        Stack<String> stack = new Stack<>();

        for (String i: s){
            if (i.equals("..")){
                if(!stack.isEmpty()){
                    stack.pop();
                }
            }
            else if(!i.equals(".") && !i.isEmpty()){
                stack.push(i);
            }
        }
        StringBuilder res = new StringBuilder("/");

        for (String i: stack){
            res.append(i).append("/");
           
        }

        if (res.length() > 1){
            res.deleteCharAt(res.length()-1);

        }

        return res.toString();

    }
}
