class Solution {
    public int mostWordsFound(String[] sentences) {
        ArrayList<String> res = new ArrayList<>();

        for (int i = 0; i < sentences.length; i++){
           res.add(sentences[i]);
        }

        int max = 0;
        for (int i = 0; i < res.size(); i++){
            String [] new_res = res.get(i).split(" ");
            max = Math.max(new_res.length, max);
        }
        return max;
    }
}
