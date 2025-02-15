class Solution {
public:
    int LCM(int n1,int n2) {
        int lcm;
        int i = 1;
        int maxnum = max(n1, n2);
        while(i)
        {
            int multiple = i * maxnum;
            if(multiple % n1 == 0 && multiple % n2 ==0)
            {
                lcm = multiple;
                break;
            }
            i = i + 1;

        }
        
       
        return lcm;

    }
};