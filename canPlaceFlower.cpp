#include <iostream>
#include <vector>
using namespace std;

class Solution{
    public:
        bool canPlaceFlower(vector<int>& flowerbed, int n) {
            int check;
            int length = flowerbed.size();
            for(int i=0; i<length; i++) {
                check = flowerbed[i];
                if(check == flowerbed[i+1]) {
                    printf("Not valid");
                }
            }
            return true;
        }
};

int main() {
    Solution sol;
    vector<int> flowerbed = {1, 0, 0, 0, 1};
    int n = 1;
    bool result = sol.canPlaceFlower(flowerbed, n);
    cout << std::boolalpha << result << endl;
    return 0;
}


/* int flowerbed[] = [1,0,0,0,1]*/
/* int n = 1, one new plant can be placed there in flowerbed[2], and it won't violet the proccess */