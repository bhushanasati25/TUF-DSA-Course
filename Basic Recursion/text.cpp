#include <bits/stdc++.h>  // Includes all standard headers
using namespace std;

bool isPalindrome(const string &str) {
    string reversedStr = str;
    reverse(reversedStr.begin(), reversedStr.end());  // reverse() is from <algorithm>
    return str == reversedStr;
}

int main() {
    string inputString;
    
    cout << "Enter a string: ";
    cin >> inputString;  // Read input from the user

    if (isPalindrome(inputString)) {
        cout << "The string \"" << inputString << "\" is a palindrome!" << endl;
    } else {
        cout << "The string \"" << inputString << "\" is NOT a palindrome!" << endl;
    }

    return 0;
}
