/*
 * ============================================
 *  그래프 최단경로 모음
 * ============================================
 *  1. 벨만-포드: 음수 간선 O.K., O(VE)
 *  2. 플로이드-워셜: 모든 쌍 최단경로, O(V³)
 *  3. 위상 정렬: DAG에서 순서 결정, O(V+E)
 */
#include <bits/stdc++.h>
using namespace std;

const int INF = 1e9;

// ===== 1. 벨만-포드 (Bellman-Ford) =====
// 음수 간선 허용, 음수 사이클 탐지 가능
struct Edge {
    int from, to, cost;
};

vector<Edge> edges;
int dist_bf[501];

bool bellman_ford(int start, int n) {
    fill(dist_bf, dist_bf + n + 1, INF);
    dist_bf[start] = 0;

    // n-1번 반복 (최단경로는 최대 n-1개 간선)
    for (int i = 0; i < n - 1; i++) {
        for (auto& e : edges) {
            if (dist_bf[e.from] != INF && dist_bf[e.from] + e.cost < dist_bf[e.to]) {
                dist_bf[e.to] = dist_bf[e.from] + e.cost;
            }
        }
    }

    // n번째 반복에서 갱신되면 → 음수 사이클 존재
    for (auto& e : edges) {
        if (dist_bf[e.from] != INF && dist_bf[e.from] + e.cost < dist_bf[e.to]) {
            return true;    // 음수 사이클 있음!
        }
    }
    return false;
}


// ===== 2. 플로이드-워셜 (Floyd-Warshall) =====
// 모든 정점 쌍 간의 최단경로
int dist_fw[501][501];

void floyd_warshall(int n) {
    // 초기화: dist[i][i] = 0, 나머지 = INF (입력 시 설정)

    for (int k = 1; k <= n; k++) {          // 경유지
        for (int i = 1; i <= n; i++) {      // 출발
            for (int j = 1; j <= n; j++) {  // 도착
                if (dist_fw[i][k] + dist_fw[k][j] < dist_fw[i][j]) {
                    dist_fw[i][j] = dist_fw[i][k] + dist_fw[k][j];
                }
            }
        }
    }
}


// ===== 3. 위상 정렬 (Topological Sort) =====
// DAG(방향 비순환 그래프)에서 순서 결정
// 진입차수(in-degree) 기반 BFS (Kahn's Algorithm)
vector<int> adj_ts[501];
int in_degree[501];

vector<int> topological_sort(int n) {
    queue<int> q;
    vector<int> result;

    // 진입차수 0인 노드 → 큐에 삽입
    for (int i = 1; i <= n; i++) {
        if (in_degree[i] == 0) q.push(i);
    }

    while (!q.empty()) {
        int cur = q.front();
        q.pop();
        result.push_back(cur);

        for (int next : adj_ts[cur]) {
            in_degree[next]--;
            if (in_degree[next] == 0) {
                q.push(next);
            }
        }
    }

    return result;  // result.size() < n 이면 사이클 존재
}

/*
 * 💡 핵심 암기 포인트:
 *   ┌──────────────┬──────────┬──────────┬───────────┐
 *   │  알고리즘     │ 시간복잡도 │ 음수 간선 │   용도     │
 *   ├──────────────┼──────────┼──────────┼───────────┤
 *   │ 다익스트라    │ O(E logV) │   ✗      │ 단일 출발   │
 *   │ 벨만-포드     │ O(VE)    │   ✓      │ 음수 사이클  │
 *   │ 플로이드-워셜  │ O(V³)    │   ✓      │ 모든 쌍     │
 *   │ 위상 정렬     │ O(V+E)   │   -      │ DAG 순서   │
 *   └──────────────┴──────────┴──────────┴───────────┘
 *
 *   1. 벨만-포드: V-1번 반복 후 V번째에서 갱신 → 음수 사이클
 *   2. 플로이드: k(경유) → i(출발) → j(도착) 순서 꼭 지키기!
 *   3. 위상 정렬: 진입차수 0 → 큐 → 인접 노드 차수 감소
 */

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    return 0;
}
