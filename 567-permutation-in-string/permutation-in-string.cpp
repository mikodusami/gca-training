class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        /**
        goal: return true if one of s1's substrings is a permutation of s2
        patterns: substring => sliding window, permutation = arrangement of all chars in string meaning we have to find a substring in s2 that has the same character count as the substring in s1, therefore frequency pops out -> unordered_map (hashmap)
        input: string 1: our main string, string2: the string of which we need to find a substring that has the same character counts of string 1
        output: boolean indicating if there is a permutation of s1 within s2
        type: sliding window (fixed or dynamic?) => fixed, window must be the size of s1 since we need to find a substring w the same char count as s1.
        edge cases: s2 must be greater or equal to s1
        constraints: 10^4 => linear-like time (linear O(n) or O(log n))
        state: frequency_of_chars_for_s1, frequency_of_chars_for_s2, window-left-boundary, window-right-boundary
        transitions:
        frequency_of_chars_for_s1: updates when collecting all chars of s1 initially
        frequeny_of_chars_for_s2: updates when collecting chars of s2 initially and when moving within the window as depending on if we have found the same arrangement, you would have tp remove a frequency from the map or add to it.
        window_left_boundary: updates when window size becomes too big or greater than the length of s1

        **/


        // initialize the hashmaps
        // initalize the size of s1 and s2
        // collect frequency of s1
        // collect frequency of s2 up to size of s1 (bc we only check the size of s1 windows)
        // loop from size-of-s2 to size-of-s1
        // -- check if the hashmaps equal each other, if true return true
        // -- add the current character to the hashmap
        // - check if the size of the window is larger than s1, if it is, repeatedly remove the first char until it is right
        
        int m = s1.size(), n = s2.size();
        if (n < m) return false;
        int windowLeft = 0;
        unordered_map<char, int> frequency_of_chars_for_s1, frequency_of_chars_for_s2;
        for (const auto& c: s1) frequency_of_chars_for_s1[c]++;
        for (int i = 0; i < m; i++) frequency_of_chars_for_s2[s2[i]]++;
        for (int i = m; i < n; i++){
            if (frequency_of_chars_for_s1 == frequency_of_chars_for_s2) return true;
            frequency_of_chars_for_s2[s2[i]]++;
            frequency_of_chars_for_s2[s2[windowLeft]]--;
            if (frequency_of_chars_for_s2[s2[windowLeft]] <= 0){
                frequency_of_chars_for_s2.erase(s2[windowLeft]);
            };
            windowLeft += 1;
        }

        return frequency_of_chars_for_s1 == frequency_of_chars_for_s2;


    }
};