class Solution {
public:
    void pattern18(int n) {
        char chr = 'A' + n - 1;
        for(int i = 0; i < n; i++)
        {
            for(char ch = chr - i; ch <= chr; ch++)
            {
                cout << ch << " ";
            }
            cout << endl;
        }

    }
};