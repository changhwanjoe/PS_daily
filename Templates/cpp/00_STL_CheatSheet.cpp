/*
 * ============================================
 *  C++ 알고리즘 자주 쓰는 입출력 & STL 패턴
 * ============================================
 *  코딩테스트에서 매번 쓰는 보일러플레이트 모음
 */
#include <bits/stdc++.h>
using namespace std;

// ===== 빠른 입출력 (필수) =====
// main 시작부에 반드시 추가
// ios::sync_with_stdio(false);
// cin.tie(nullptr);

// ===== 자주 쓰는 자료구조 =====
void stl_examples() {
    // --- vector ---
    vector<int> v = {3, 1, 4, 1, 5};
    sort(v.begin(), v.end());                   // 오름차순 정렬
    sort(v.begin(), v.end(), greater<>());       // 내림차순 정렬
    v.erase(unique(v.begin(), v.end()), v.end()); // 중복 제거 (정렬 후)

    // --- map ---
    map<string, int> mp;
    mp["apple"] = 3;
    for (auto& [key, val] : mp) { /* ... */ }   // C++17

    // --- set ---
    set<int> s = {3, 1, 4};                     // 자동 정렬, 중복 없음
    s.count(3);     // 존재 여부 (0 or 1)

    // --- priority_queue ---
    priority_queue<int> maxPQ;                          // 최대 힙 (기본)
    priority_queue<int, vector<int>, greater<>> minPQ;  // 최소 힙

    // --- deque ---
    deque<int> dq;
    dq.push_front(1); dq.push_back(2);
    dq.pop_front();    dq.pop_back();

    // --- pair / tuple ---
    pair<int, int> p = {1, 2};
    auto [a, b] = p;                    // C++17 구조적 바인딩
    tuple<int, int, int> t = {1, 2, 3};
    auto [x, y, z] = t;
}

// ===== 자주 쓰는 알고리즘 함수 =====
void useful_functions() {
    vector<int> v = {3, 1, 4, 1, 5, 9};

    // 최대/최소
    int mx = *max_element(v.begin(), v.end());
    int mn = *min_element(v.begin(), v.end());

    // 이분 탐색 (정렬된 배열)
    sort(v.begin(), v.end());
    bool found = binary_search(v.begin(), v.end(), 4);
    auto it = lower_bound(v.begin(), v.end(), 4);   // 4 이상 첫 위치
    int idx = it - v.begin();

    // 순열
    sort(v.begin(), v.end());
    do {
        // v의 모든 순열 처리
    } while (next_permutation(v.begin(), v.end()));

    // 누적합
    vector<int> prefix(v.size() + 1, 0);
    for (int i = 0; i < (int)v.size(); i++)
        prefix[i + 1] = prefix[i] + v[i];
    // 구간 [l, r] 합 = prefix[r+1] - prefix[l]

    // 문자열 → 정수, 정수 → 문자열
    int num = stoi("123");
    string s = to_string(456);

    // GCD (C++17)
    int g = __gcd(12, 8);   // 4
}

// ===== 2D 배열 입력 패턴 =====
int grid[1001][1001];

void read_grid() {
    int n, m;
    cin >> n >> m;
    for (int i = 0; i < n; i++)
        for (int j = 0; j < m; j++)
            cin >> grid[i][j];
}

/*
 * 💡 핵심 암기 포인트:
 *   1. ios::sync_with_stdio(false); cin.tie(nullptr); → 필수!
 *   2. endl 대신 "\n" 사용 (endl은 flush 발생 → 느림)
 *   3. 최소 힙: priority_queue<int, vector<int>, greater<>>
 *   4. auto& [k, v] : map → C++17 구조적 바인딩
 *   5. lower_bound 결과 인덱스 = it - v.begin()
 */

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    return 0;
}
