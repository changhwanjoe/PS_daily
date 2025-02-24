#include <iostream>
using namespace std;

int main(void) {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int M = 0;
    int N = 0;
    int s[100001] = {}; //0으로 초기화

    cin >> N >> M;
    for (int i = 1; i <= N; i++) {
        int temp = 0;
        cin >> temp;
        s[i] = s[i - 1] + temp;
    }
    for (int i = 1; i <= M; i++) {
        int start, end;
        cin >> start >> end;
        cout << s[end] - s[start - 1] << '\n';
    }
    return 0;
}