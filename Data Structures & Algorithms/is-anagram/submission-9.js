class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) 
    {
        if (s.length !== t.length)
        {
            return false
        }

        const d= new Map() //dictionary
        for (const c of s)
        {
            d.set(c, (d.get(c) ?? 0) + 1)
        }

        for (const c of t)
        {
            d.set(c, (d.get(c)?? 0)- 1)
        }

        for (const v of d.values()){
            if (v!==0){
                return false
            }
        }

        return true
    }
}
