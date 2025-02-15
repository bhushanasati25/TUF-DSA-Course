class Solution {
public:
    int countOddDigit(int n) {
        int countodd = 0;
        while(n>0)
        {
            int lastdigit = n % 10;
            if(lastdigit % 2 == 1)
            {
                countodd = countodd + 1;
                
            }
            n = n / 10;
            
        }
        return countodd;

    }
};