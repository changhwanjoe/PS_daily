/*
 * ============================================
 *  다익스트라 (Dijkstra) — 단일 출발 최단경로
 * ============================================
 *  시간복잡도: O(E log V)  (우선순위 큐 사용)
 *  조건: 음수 간선 없음
 *
 *  핵심: priority_queue에 (거리, 노드) 넣고
 *        거리가 짧은 것부터 꺼내서 갱신
 */
#include <bits/stdc++.h>
using namespace std;

const int INF = 1e9;
const int MAX = 100001;

vector<pair<int, int>> adj[MAX];    // adj[u] = {(v, weight), ...}
int dist[MAX];

void dijkstra(int start, int n) {
    fill(dist, dist + n + 1, INF);
    // min-heap: {거리, 노드}
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> pq;

    dist[start] = 0;
    pq.push({0, start});

    while (!pq.empty()) {
        auto [d, cur] = pq.top();
        pq.pop();

        if (d > dist[cur]) continue;    // 이미 더 짧은 경로로 방문됨 → 스킵

        for (auto [next, weight] : adj[cur]) {
            int cost = d + weight;
            if (cost < dist[next]) {
                dist[next] = cost;
                pq.push({cost, next});
            }
        }
    }
}

/*
 * 💡 핵심 암기 포인트:
 *   1. priority_queue<..., greater<>> → 최소 힙 (기본은 최대 힙!)
 *   2. if (d > dist[cur]) continue; → 이미 처리된 노드 스킵 (필수)
 *   3. dist 배열 INF로 초기화
 *   4. 음수 간선 있으면 → 벨만-포드 사용
 */

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, start;
    cin >> n >> m >> start;

    for (int i = 0; i < m; i++) {
        int u, v, w;
        cin >> u >> v >> w;
        adj[u].push_back({v, w});
    }

    dijkstra(start, n);

    for (int i = 1; i <= n; i++) {
        if (dist[i] == INF) cout << "INF\n";
        else cout << dist[i] << "\n";
    }

    return 0;
}
