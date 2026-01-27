class Solution {
public:
    bool isAnagram(string s, string t) {
        /**
        constraints: N < 10^4 = linear time
        pattern recognition: "anagram" means hashmap
        input: two strings (s and t)
        output: true if t is an anagram of s
        goal: determine if t is an anagram of s meaning if t and s can = the same word if the letters are arranged
        state: hashmap = {} 
        transition: 
        - IF S[LETTER] in HASHMAP: Reduce by 1
        - IF S[LETTER] not in HASHMAP: return false
        - IF S[LETTER] in HASHMAP and REDUCING by 1 is less than 0, return false
        **/
        if (s.size() != t.size()) return false;
        unordered_map<char, int> map;
        for (const auto& letter: s) map[letter]++;
        for (const auto& letter: t){
            if (!map.contains(letter) || map[letter] == 0) return false;
            map[letter] -= 1;
        }
        return true;
    }
};