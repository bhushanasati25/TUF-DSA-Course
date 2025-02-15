class Solution {
private:
 bool isPrime(int n) {
        //your code goes here
        if(n == 1)
        {
            return false;
        }
        for(int i = 2; i * i <= n; i++)
        {
            if(n % i == 0)
            {
                return false;
            }
        }
        return true;

    }
public:
    int primeUptoN(int n) {
        int count = 0;
        for(int i = 2; i <= n; i++)
        {
            if(isPrime(i))
            {
                count = count + 1;
            }
        }
        return count;

    }
};