class Solution {
public:
    bool isPerfect(int n) {
        int sum = 0;
        for(int i = 1; i <= n-1; i++)
        {
            if(n % i == 0)
            {
                sum = sum + i;
            }
        }
        return (sum == n);

    }
};