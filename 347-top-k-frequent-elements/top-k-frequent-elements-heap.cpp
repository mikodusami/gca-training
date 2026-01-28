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

        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> heap;

        for (const auto& entry : count) {
            heap.push({entry.second, entry.first});
            if (heap.size() > k) {
                heap.pop();
            }
        }

        vector<int> res;
        for (int i = 0; i < k; i++)
        {
            res.push_back(heap.top().second);
            heap.pop();
        }

        return res;
    }
};
