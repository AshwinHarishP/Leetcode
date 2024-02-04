class Solution {
    public String minWindow(String s, String t) {
        if (t.equals("")) return "";

        Map<Character, Integer> countT = new HashMap<>();
        Map<Character, Integer> windowT = new HashMap<>();

        for (char i : t.toCharArray()) {
            countT.put(i, 1 + countT.getOrDefault(i, 0));
        }

        int have = 0;
        int need = countT.size();
        int resLen = Integer.MAX_VALUE;
        int[] res = new int[]{-1, -1};
        int l = 0;

        for (int r = 0; r < s.length(); r++) {
            char c = s.charAt(r);
            windowT.put(c, 1 + windowT.getOrDefault(c, 0));

            if (countT.containsKey(c) && windowT.get(c).equals(countT.get(c))) {
                have++;
            }

            while (have == need) {
                if ((r - l + 1) < resLen) {
                    res[0] = l;
                    res[1] = r;
                    resLen = (r - l + 1);
                }

                windowT.put(s.charAt(l), windowT.get(s.charAt(l)) - 1);
                if (countT.containsKey(s.charAt(l)) && windowT.get(s.charAt(l)) < countT.get(s.charAt(l))) {
                    have--;
                }

                l++;
            }
        }

        int left = res[0];
        int right = res[1];
        return left != -1 ? s.substring(left, right + 1) : "";
    }
}
