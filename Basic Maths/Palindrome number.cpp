class Solution {
private:
int reverseNumber(int n) {
        int revnum = 0;
        while(n>0)
        {
            int lastdigit = n%10;
            revnum = (revnum * 10) + lastdigit;
            n = n/10;

        }
        return revnum;

    }

public:
    bool isPalindrome(int n) {
       int revnumber = reverseNumber(n);

       return (n == revnumber); 


    }
};