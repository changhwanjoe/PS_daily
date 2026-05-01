/*
 * ============================================
 *  최소 스패닝 트리 (MST) — 크루스칼 & 프림
 * ============================================
 *  크루스칼: 간선 정렬 + Union-Find, O(E log E)
 *  프림: 우선순위 큐, O(E log V)
 */
#include <bits/stdc++.h>
using namespace std;

int parent[100001], rnk[100001];
void init(int n) { for (int i = 0; i <= n; i++) { parent[i] = i; rnk[i] = 0; } }
int find(int x) { return parent[x] == x ? x : parent[x] = find(parent[x]); }
bool unite(int a, int b) {
    a = find(a); b = find(b);
    if (a == b) return false;
    if (rnk[a] < rnk[b]) swap(a, b);
    parent[b] = a;
    if (rnk[a] == rnk[b]) rnk[a]++;
    return true;
}

struct Edge {
    int cost, u, v;
    bool operator<(const Edge& o) const { return cost < o.cost; }
};

// 크루스칼: 간선 정렬 → Union-Find → n-1개 선택
long long kruskal(int n, vector<Edge>& edges) {
    sort(edges.begin(), edges.end());
    init(n);
    long long total = 0;
    int cnt = 0;
    for (auto& e : edges) {
        if (unite(e.u, e.v)) {
            total += e.cost;
            if (++cnt == n - 1) break;
        }
    }
    return total;
}

/*
 * 💡 핵심: 간선 정렬 → 사이클 아니면 선택 → MST 간선 = V-1개
 */

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, m; cin >> n >> m;
    vector<Edge> edges(m);
    for (auto& e : edges) cin >> e.u >> e.v >> e.cost;
    cout << kruskal(n, edges) << "\n";
}
