class Solution {
    public int mostWordsFound(String[] sentences) {
        
        int max = 0;
        for (int i = 0; i < sentences.length; i++){
           String [] new_res = sentences[i].split(" ");
           max = Math.max(new_res.length, max);
        }
        return max;
    }
}
