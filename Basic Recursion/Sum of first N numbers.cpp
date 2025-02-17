class Solution{	
	public:
		int NnumbersSum(int N){
			//your code goes here
            int sum = 0;
            for(int i = 0; i <=N; i++)
            {
                sum = sum + i;
            }
            return sum;
		}
};