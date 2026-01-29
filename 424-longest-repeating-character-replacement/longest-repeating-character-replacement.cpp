class Solution {
public:
    int characterReplacement(string s, int k) {
        /**
        pattern recognition: substring => sliding window
        - fixed or dynamic? dynamic, grows based on replacement
        goal: return the length of the longest substring that is the same letter after making k replacements
        understanding some concepts:
        - The Replacements: in a given window of characters, we can make from 1-k replacements of a nother letter to ensure it equals another one. We know which letter to change based on the most frequent letter in the window since the most frequent letter is the one with the most frequency. To do the actual replacements, we may not need to actually replace the letters but keep track of how many replacements we have made and once we have no more, we need to contract the window.
        = What is the condition for the sliding windpw? We have window size, we have most frequent letter (the number), we have k, left substring. Well we can make max k changes right, so we decrease the size of the window once we have no more changes so that means somethng is > k , so if (windowlength - mostfrequtnletternumber) < k, it means we have run out of changes and therefore we can move the left side of the window up until we have enough changes
        state: left pointer, right pointer (forloop), unordered map, highest_frequency, 
        transitions:
        - leftpointer: updates(+) when the slding window condition is true ((r - l + 1) - highestfreq > k)
        - map: used to track the freqency of the current window
        - highest_frequency: updated once we track a numbers frequency, we take the max of whatever the current frequency is for this number
        - longestLength: ...

        **/
        // string s, int k
        unordered_map<char, int> window_freq;
        int window_highest_freq = 0;
        int left = 0;
        int length = 0;
        for (int r = 0; r < s.size(); r++)
        {
            window_freq[s[r]] += 1;
            window_highest_freq = max(window_highest_freq, window_freq[s[r]]);
            while ((r - left + 1) - window_highest_freq > k)
            {
                window_freq[s[left]] -= 1;
                window_highest_freq = max(window_highest_freq, window_freq[s[left]]);
                left += 1;
            }


            length = max(length, r - left + 1);
        }   

        return length;
    }
};