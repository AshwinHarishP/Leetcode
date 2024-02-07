class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> res = new ArrayList<>();
        if (strs == null || strs.length == 0){
            return res;
        }

        HashMap<String, List<String>> group = new HashMap<>();

        for (String i: strs){
            char [] ch = i.toCharArray();
            Arrays.sort(ch);
            String sorted_ele = new String(ch);

            if (group.containsKey(sorted_ele)){
                group.get(sorted_ele).add(i);
            }
            else{
                List<String> ls = new ArrayList<>();
                ls.add(i);
                group.put(sorted_ele, ls);
            }
        }
        res.addAll(group.values());
        return res;

    }
}
