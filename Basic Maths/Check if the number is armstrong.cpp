class Solution {
public:
    bool isArmstrong(int n) {
        int sum = 0;
        int count = log10(n) + 1;
        int duplicate = n;
        while(n > 0)
        {
            int lastdigit = n % 10;
            sum = sum + pow(lastdigit,count);

            n = n /10;
        }
        return (duplicate == sum);

    }
};