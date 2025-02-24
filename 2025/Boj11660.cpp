#include <iostream>
using namespace std;

#include <vector>
// Todo : 0,0 부터 x,y 까지 합을 구하는 D[x][y]를 만들어서 누적합을 저장해놓는다.
// Todo2 : 범위에 대해서 구한다

int main(void) {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int M = 0;
    int N = 0;

    cin >> N >> M;
    vector<vector<int>> A(N + 1, vector<int>(N + 1, 0)); // 0으로 초기화된 N+1 x N+1 2차원 벡터 
    vector<vector<int>> D(N + 1, vector<int>(N + 1, 0));

    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= N; j++) {
            int temp = 0;
            cin >> A[i][j];
            D[i][j] = D[i - 1][j] + D[i][j - 1] - D[i-1][j-1]+ A[i][j];
        }
    }
    for (int i = 1; i <= M; i++) {
        int x1, y1, x2, y2;
        cin >> x1 >> y1 >> x2 >> y2;
        int result = D[x2][y2] - D[x1 - 1][y2] - D[x2][y1 - 1] + D[x1 - 1][y1 - 1];
        cout << result << '\n';
    }
    return 0;
}