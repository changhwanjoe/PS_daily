#include <string>
#include <vector>
#include <queue>
#include <iostream>

using namespace std;
int com_num = 0;
queue<int> q;
vector<int> visited = { 0, };

void bfs(int n, vector<vector<int>> computers, int x) {
    q.push(x);
    while (!q.empty()) {
        int nx = q.front();
        q.pop();

        if (visited[nx] == 1)continue;
        if (nx == n - 1) continue;
        for (int i = x + 1; i < n; i++) {
            if (computers[x][i] == 1)
            {
                q.push(i);
            }
        }
        visited[x] = 1;
    }
}

int solution(int n, vector<vector<int>> computers) {
    int answer = 0;
    for (int i = 0; i < n; i++) {
        if (visited[i] != 1) {
            bfs(n, computers, i);
            answer += 1;
        }
    }
    return answer;
}

int main(void) {
    int n = 3;
    vector<vector<int>> computers = { {1, 1, 0},{1, 1, 0},{0, 0, 1} };
    visited.resize(n);
    cout << solution(n, computers) << endl;
}