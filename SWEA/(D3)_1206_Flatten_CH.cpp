#include <iostream> 
#include <algorithm>

using namespace std;

int main(void)
{
    int T = 0;
    int t = 0;
    int result = 0;

    for (int i = 0; i < 10; i++) {
        cin >> T;
        int arr[100] = { 0, };
        for (int l = 0; l < 100; l++) {
            cin >> t;
            arr[l] = t;
        }

        for (int j = 0; j < T; j++) {
            sort(arr, arr + 100);
            for (int k = 0; k < 100; k++) {
            //    cout << arr[k];
            }
            if (arr[99] == arr[0]) {
                cout << "#" << i << " " << 0 << endl;
                cout << "hello wolrd" << endl;
                return 0;
            }
            else {
                arr[99] -= 1;
                arr[0] += 1;
            }
        sort(arr, arr + 100);
        result = arr[99] - arr[0];

        }
    cout << "#" << i + 1 << " " << result << endl;
    }
}

