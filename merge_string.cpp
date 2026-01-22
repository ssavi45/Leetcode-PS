/*leetcode problem-1768: Merge string alternatively*/ 

#include <string>
#include <iostream>

using namespace std;

class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        int n1 = word1.length();
        int n2 = word2.length();

        string result_string = "";
        int i = 0;

        while (i<n1 || i<n2) {
            if(i<n1) {
                result_string = result_string + word1[i];
            }
            if(i<n2) {
                result_string = result_string + word2[i];
            }
            i++;
        }
        return result_string;
    }
};

int main() {
        Solution sol;
        string word1 = "abcd";
        string word2 = "pq";
        string merged_string = sol.mergeAlternately(word1, word2);
        cout << merged_string << endl; // Output: "apbqcd"
        return 0;
    }