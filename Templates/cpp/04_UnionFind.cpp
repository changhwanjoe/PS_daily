/*
 * ============================================
 *  Union-Find (분리 집합, Disjoint Set Union)
 * ============================================
 *  시간복잡도: O(α(N)) ≈ O(1) (아커만 역함수)
 *
 *  용도: 그룹 합치기, 같은 그룹 판별, 크루스칼 MST
 *  핵심: find (경로 압축) + union (랭크 기반)
 */
#include <bits/stdc++.h>
using namespace std;

const int MAX = 100001;
int parent[MAX];
int rnk[MAX];       // rank는 예약어와 충돌 방지

// 초기화
void init(int n) {
    for (int i = 0; i <= n; i++) {
        parent[i] = i;
        rnk[i] = 0;
    }
}

// Find (경로 압축)
int find(int x) {
    if (parent[x] != x)
        parent[x] = find(parent[x]);    // 재귀적 경로 압축
    return parent[x];
}

// Union (랭크 기반)
bool unite(int a, int b) {
    a = find(a);
    b = find(b);

    if (a == b) return false;   // 이미 같은 그룹

    // 랭크가 낮은 트리를 높은 트리 아래에 붙임
    if (rnk[a] < rnk[b]) swap(a, b);
    parent[b] = a;
    if (rnk[a] == rnk[b]) rnk[a]++;

    return true;
}

// 같은 그룹인지 판별
bool is_same(int a, int b) {
    return find(a) == find(b);
}

/*
 * 💡 핵심 암기 포인트:
 *   1. parent[i] = i 로 초기화 (자기 자신이 루트)
 *   2. find: 경로 압축 → parent[x] = find(parent[x])
 *   3. union: 랭크 기반 합치기 → 트리 높이 최소화
 *   4. 크루스칼 MST: 간선 정렬 후 union-find로 사이클 판별
 */

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;
    init(n);

    for (int i = 0; i < m; i++) {
        int cmd, a, b;
        cin >> cmd >> a >> b;
        if (cmd == 0) {
            unite(a, b);
        } else {
            cout << (is_same(a, b) ? "YES" : "NO") << "\n";
        }
    }

    return 0;
}
