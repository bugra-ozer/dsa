class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {

        HashMap<String, ArrayList<String>> dict = new HashMap<>();

        for (String s : strs){
            char[] chars = s.toCharArray();
            Arrays.sort(chars);
            String key = new String(chars);

            if (dict.containsKey(key)){
                dict.get(key).add(s);
            } else {
                ArrayList<String> arr = new ArrayList<>();
                dict.put(key, arr);
                dict.get(key).add(s);
            }
        }

        ArrayList<List<String>> res = new ArrayList<>();
        for (ArrayList<String> v : dict.values()){
            res.add(v);
        }
        return res;
    }
}
