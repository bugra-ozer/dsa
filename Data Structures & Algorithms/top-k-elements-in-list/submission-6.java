class Solution {
    public int[] topKFrequent(int[] nums, int k) {

        HashMap<Integer, Integer> dict = new HashMap<>();

        for (Integer n : nums){
            dict.put(n, dict.getOrDefault(n, 0)+1);
        }

        HashMap<Integer, List<Integer>> invDict = new HashMap<>();

        for (Map.Entry<Integer, Integer> e : dict.entrySet()){
            Integer key = e.getValue();
            Integer val = e.getKey();
            
            if (invDict.containsKey(key)){
                invDict.get(key).add(val);
            }
            else {
                invDict.put(key, new ArrayList<Integer>());
                invDict.get(key).add(val);
            }
        }

        ArrayList<Integer> keys = new ArrayList<>(invDict.keySet());
        keys.sort(Collections.reverseOrder());

        ArrayList<Integer> winners = new ArrayList<>();
        for (Integer n : keys){
            Integer need = k - winners.size();
            if (winners.size() < k){
                Integer take = Math.min(need, invDict.get(n).size());
                winners.addAll(invDict.get(n).subList(0, take));
            }
        }

        int[] result = new int[winners.size()];
        for (Integer i = 0; i<winners.size(); i++){
            result[i]= winners.get(i);
        }
        
        return result;
    }
}