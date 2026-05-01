/*
 * ============================================
 *  BFS (너비 우선 탐색) & DFS (깊이 우선 탐색)
 * ============================================
 *  시간복잡도: O(V + E)  (정점 + 간선)
 *  공간복잡도: O(V)
 *
 *  BFS: 최단거리, 레벨별 탐색 → queue
 *  DFS: 경로 탐색, 백트래킹, 사이클 탐지 → stack/재귀
 */
#include <bits/stdc++.h>
using namespace std;

const int MAX = 100001;
vector<int> adj[MAX];   // 인접 리스트
bool visited[MAX];

// ===== BFS =====
void bfs(int start) {
    queue<int> q;
    q.push(start);
    visited[start] = true;

    while (!q.empty()) {
        int cur = q.front();
        q.pop();
        // cur 처리 (출력, 거리 계산 등)

        for (int next : adj[cur]) {
            if (!visited[next]) {
                visited[next] = true;
                q.push(next);
            }
        }
    }
}

// ===== DFS (재귀) =====
void dfs(int cur) {
    visited[cur] = true;
    // cur 처리

    for (int next : adj[cur]) {
        if (!visited[next]) {
            dfs(next);
        }
    }
}

// ===== DFS (스택, 비재귀) =====
void dfs_iterative(int start) {
    stack<int> st;
    st.push(start);

    while (!st.empty()) {
        int cur = st.top();
        st.pop();

        if (visited[cur]) continue;
        visited[cur] = true;
        // cur 처리

        for (int next : adj[cur]) {
            if (!visited[next]) {
                st.push(next);
            }
        }
    }
}

// ===== 2D 격자 BFS (최단거리) =====
int dist[1001][1001];
int dx[] = {-1, 1, 0, 0};  // 상하좌우
int dy[] = {0, 0, -1, 1};

void bfs_grid(int sx, int sy, int N, int M, int grid[][1001]) {
    memset(dist, -1, sizeof(dist));
    queue<pair<int, int>> q;
    q.push({sx, sy});
    dist[sx][sy] = 0;

    while (!q.empty()) {
        auto [x, y] = q.front();   // C++17 구조적 바인딩
        q.pop();

        for (int d = 0; d < 4; d++) {
            int nx = x + dx[d];
            int ny = y + dy[d];

            if (nx < 0 || nx >= N || ny < 0 || ny >= M) continue;  // 범위 체크
            if (dist[nx][ny] != -1) continue;                       // 방문 체크
            if (grid[nx][ny] == 0) continue;                        // 벽 체크

            dist[nx][ny] = dist[x][y] + 1;
            q.push({nx, ny});
        }
    }
}

/*
 * 💡 핵심 암기 포인트:
 *   1. BFS = queue, DFS = stack(또는 재귀)
 *   2. BFS는 방문 체크를 "큐에 넣을 때" 해야 중복 방문 방지
 *   3. 격자 BFS: dx/dy 배열 + 범위 체크 패턴 외우기
 *   4. 최단거리 = BFS (가중치 없는 그래프)
 */

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);    // 무방향 그래프
    }

    bfs(1);
    return 0;
}
