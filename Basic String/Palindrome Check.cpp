class Solution{	
	public:		
		bool palindromeCheck(string& s){
			//your code goes 
			int l = 0;
			int n = s.length() - 1;
			while(l <n)
			{
				if(s[l] != s[n])
				{
					return false;
				}
				l++,n--;
				
			}
			return true;
		}
};