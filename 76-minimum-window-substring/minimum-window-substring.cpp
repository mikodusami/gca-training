class Solution {
public:
    string minWindow(string s, string t) {
        int m = s.size(), n = t.size();
        /**
        pattern recoginition: substring => sliding window

        subproblems:
        1. what is the minimum window string? = a substr in s containing all letters of t with the smallest size since there can be multiple letters included.

        2. how to determine when we have a valid substring? = we have a valid substring when we have found a substring that contains all letters of t in s.

        3. how to look for this substring? = so, what if we have a left pointer and a right pointer. we update the left pointer until we encounter a letter in t (is s[l] in set(t)) and if it is, we can hold the left pointer. Then we update the right pointer (moves on its own forward) until all letters in t have been found. Once we know it has been found, we keep moving forward with right ptr until we find a char that is not in set(t) handling duplicates. Once we stop the right ptr, we save the current string that has been building to minString, then we reset the state variables and update left pointer to the current position to start a new sequence.

        4. how do we know all letters in t have been found? we can hold a variable called matches, which we know we have all matches when matches >= t.size(), this resets as well.

        4. what type of sliding window is this? = dynamic window

        5. what determines whehter we add more characters or reduce characters to the substring? = we stop adding characters once we have more matches than the size of t && the current letter is not in t.

        state: matches_map, left pointer, right pointer, t_map, minstring, current_string
        transitions:
        matches => updates when we have encountered a letter in t_map that is in the current window we are examining. decreases when we move the pointer up.
        ...

        **/

        if (n <= 0) return "";
        unordered_map<char, int> t_map, matches_map;
        for (const auto& c: t) t_map[c]++;

        int have = 0, need = t_map.size();
        pair<int, int> res = {-1, -1};
        int resLen = INT_MAX;
        int r_beg = INT_MAX;
        int l = 0;
        for (int r = 0; r < m; r++){
            char c = s[r];
            matches_map[c]++;
            if (t_map.count(c) && matches_map[c] == t_map[c]){
                have++; // we have found the same freq of chars in s
            }
            while (have == need){
                if ((r - l + 1) < resLen){
                    resLen = r - l + 1;
                    // res = {l, r};
                    r_beg = l;
                }

                matches_map[s[l]]--;
                if (t_map.count(s[l]) && matches_map[s[l]] < t_map[s[l]]) have--;
                l++;
            }
        }
        
        return resLen == INT_MAX ? "" : s.substr(r_beg, resLen);
    }
};