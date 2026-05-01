/*
 * ============================================
 *  세그먼트 트리 (Segment Tree)
 * ============================================
 *  시간복잡도: 구간 쿼리 O(log N), 점 갱신 O(log N)
 *  용도: 구간 합, 구간 최솟값/최댓값
 */
#include <bits/stdc++.h>
using namespace std;

const int MAX = 100001;
long long tree[4 * MAX];
int arr[MAX];

// 트리 구축: node가 [start, end] 구간을 담당
long long build(int node, int start, int end) {
    if (start == end) return tree[node] = arr[start];
    int mid = (start + end) / 2;
    return tree[node] = build(node * 2, start, mid) + build(node * 2 + 1, mid + 1, end);
}

// 점 갱신: idx 위치의 값을 val로 변경
void update(int node, int start, int end, int idx, long long val) {
    if (idx < start || idx > end) return;
    if (start == end) { tree[node] = val; return; }
    int mid = (start + end) / 2;
    update(node * 2, start, mid, idx, val);
    update(node * 2 + 1, mid + 1, end, idx, val);
    tree[node] = tree[node * 2] + tree[node * 2 + 1];
}

// 구간 쿼리: [l, r] 구간 합
long long query(int node, int start, int end, int l, int r) {
    if (r < start || end < l) return 0;             // 범위 밖
    if (l <= start && end <= r) return tree[node];   // 완전히 포함
    int mid = (start + end) / 2;
    return query(node * 2, start, mid, l, r) + query(node * 2 + 1, mid + 1, end, l, r);
}

/*
 * 💡 핵심 암기 포인트:
 *   1. 트리 크기 = 4 * N
 *   2. 자식: node*2 (왼쪽), node*2+1 (오른쪽)
 *   3. build: 리프에 값 저장, 올라가며 합산
 *   4. query: 범위 밖→0, 완전포함→tree[node], 아니면→분할
 *   5. update: 리프까지 내려가서 갱신, 올라오며 재계산
 */

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n, q;
    cin >> n >> q;
    for (int i = 1; i <= n; i++) cin >> arr[i];
    build(1, 1, n);
    while (q--) {
        int type; cin >> type;
        if (type == 1) { int i; long long v; cin >> i >> v; update(1, 1, n, i, v); }
        else { int l, r; cin >> l >> r; cout << query(1, 1, n, l, r) << "\n"; }
    }
}
