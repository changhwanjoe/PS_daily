#include<iostream>
using namespace std;
 
long long int arr[1000000 + 1];
int main() {
    int T;
    cin >> T;
    int ans[10];
    for (int i = 0; i < T; i++) {
        int num;
        cin >> num;
        for (int j = 0; j < num; j++) {
            cin >> arr[j];
        }
        long long int max = arr[num-1];
        long long int cnt = 0;
        for (int j = num-2; j >= 0; j--) { 
            if (arr[j] >= max)
                max = arr[j];
            else
                cnt += max - arr[j];
        }
        cout << "#" << i + 1 << " " << cnt << "\n";
    }
     
}
