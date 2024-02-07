public class Solution {
    public String frequencySort(String s) {
        // Create a HashMap to count the frequency of characters
        HashMap<Character, Integer> count = new HashMap<>();
        for (char ch : s.toCharArray()) {
            count.put(ch, count.getOrDefault(ch, 0) + 1);
        }

        // Convert the HashMap to a list of pairs (character, frequency)
        List<Pair<Character, Integer>> ls = new ArrayList<>();
        for (Map.Entry<Character, Integer> entry : count.entrySet()) {
            ls.add(new Pair<>(entry.getKey(), entry.getValue()));
        }

        // Sort the list of pairs based on the frequency in descending order
        Collections.sort(ls, new Comparator<Pair<Character, Integer>>() {
            @Override
            public int compare(Pair<Character, Integer> p1, Pair<Character, Integer> p2) {
                return Integer.compare(p2.getValue(), p1.getValue());
            }
        });

        // Construct the result string
        StringBuilder res = new StringBuilder();
        for (Pair<Character, Integer> pair : ls) {
            char ch = pair.getKey();
            int freq = pair.getValue();
            res.append(String.valueOf(ch).repeat(freq));
        }

        return res.toString();
    }
}
    
