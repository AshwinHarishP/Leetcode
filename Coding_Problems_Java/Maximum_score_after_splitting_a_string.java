class Solution {
    public int maxScore(String s) {

        int maxi = 0, left = 0;
        int right = Count(s, '1');
        
        for (int i = 0; i < s.length()-1; i++){
            if (s.charAt(i) == '0') left ++;
            else right --;
            maxi = Math.max(maxi, left + right);
        }
        return maxi;
    }
        
    public int Count(String  s, char target){
            int count = 0;
            for (char c: s.toCharArray()){
                if (c == target){
                    count ++;
                }
            }
            return count;
        }
        
    }
