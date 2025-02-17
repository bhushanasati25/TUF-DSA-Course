class Solution{	
public:		
    string largeOddNum(string& s){
        //your code goes here
		   int ind = -1;
    
        int i;
        for (i = s.length() - 1; i >= 0; i--) {
            if ((s[i] - '0') % 2 == 1) {
                ind = i;
                break;
            }
        }
        
        i = 0;
        while(i <= ind && s[i] == '0') i++;
        

        return s.substr(i, ind - i + 1);
    }
};