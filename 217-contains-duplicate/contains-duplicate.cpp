class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        /** 
        pattern recognition words: "appears at least twice in array" -> hashmap/hashset
        constraint: n <= 10^5 indicating O(n)
        input: an array of integers
        output: true if there is a duplicate value, false otherwise
        state variable: hashset = {} to hold each number
        transition states:
        - IF a number is not in the set: add to set
        - IF a number is in the set: return true since it has been found

        
        **/

        unordered_set<int> set;
        for (const auto& number: nums) {
            if (set.count(number)) return true;
            set.insert(number);
        }
        return false;
    }
};