class Solution {
    public boolean isAnagram(String s, String t){
        if (s.length() != t.length()){ //check if args different size
            return false;
        }

        HashMap<Character, Integer> dict = new HashMap<>();

        for (Character n : s.toCharArray()){
            dict.put(n, dict.getOrDefault(n, 0)+1);
        }

        for (Character n : t.toCharArray()){
            dict.put(n, dict.getOrDefault(n, 0)-1);
        }

        for (int v : dict.values()){
            if (v>0){
                return false;
            }
        }

        return true;

    }
}
