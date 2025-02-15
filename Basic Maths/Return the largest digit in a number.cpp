class Solution {
public:
    int largestDigit(int n) {
        int largest = 0;
        while(n > 0)
        {
            int lastdigit = n % 10;
            if(lastdigit > largest)
            {
                largest = lastdigit;
                
            }
            n = n/10;

        }
        return largest;


    }
};