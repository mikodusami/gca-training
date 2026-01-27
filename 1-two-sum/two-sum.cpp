class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        /***
        pattern list: indices of two numbers => two pointer
        constraints: n <= 10^4 | n2 solution
        input: array of numbers, a target
        output: 2 element array of indices of which nums[output[0]] + nums[output[1]] == target
        state: the array - input array
        transition:
        IF number is found in inner loop where target - numver == nunber in outer loop, returb


        **/
        for (int i = 0; i < nums.size(); i++) {
            for (int j = i + 1; j < nums.size(); j++) {
                if (nums[i] + nums[j] == target) {
                    return {i, j};
                }
            }
        }
        return {};


        return vector<int>();
    }
};