#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    /* Function to get the sum of highest
    and lowest frequency in array */
    int sumHighestAndLowestFrequency(vector<int> &nums) {
        
        // Variable to store the size of array
        int n = nums.size();
        
        /* Variable to store maximum 
        and minimum frequency */
        int maxFreq = 0;
        int minFreq = n;

        // Visited array
        vector<bool> visited(n, false);
        
        // First loop
        for(int i = 0; i < n; i++) {
            // Skip second loop if already visited
            if(visited[i]) continue;
            
            /* Variable to store frequency
            of current element */
            int freq = 0;
            
            // Second loop
            for(int j = i; j < n; j++) {
                if(nums[i] == nums[j]) {
                    freq++;
                    visited[j] = true;
                }
            }
            
            /* Update maximum and 
            minimum frequencies */
            maxFreq = max(maxFreq, freq);
            minFreq = min(minFreq, freq);
        }
        
        // Return the required sum
        return maxFreq+minFreq;
    }
};
