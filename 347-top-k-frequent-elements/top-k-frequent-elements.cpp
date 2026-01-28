class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        /**
        pattern: most frequent => two pointer
        constraints: n <= 5 so an o(n)
        input: an array of inteegrs, and inteer k representing the amount fo elements to return
        state: an unordered map, a vector of pairs, a vector for result
        transitions (What specific events forces me to update my data structure)
        - HASHMAP: WE UPDATE IT WHEN COLLECTING THE FREQUENCY
        - ARRPAIRS: WE PUSH A PAIR OF {FREQ:NUM} IN THE ARRAY
        - RES: WE PUSHBACK THE NUMBERS IN ARRPAIRS STARTING FROM BACK
        **/

        unordered_map<int, int> count;
        for (const int& num: nums) {
            count[num]++;
        }

        vector<pair<int, int>> arr;
        for (const auto& p : count) {
            arr.push_back({p.second, p.first});
        }
        sort(arr.rbegin(), arr.rend());
        vector<int> res;
        for (int i = 0; i < k; i++){
            res.push_back(arr[i].second);
        }
        return res;
    }
};