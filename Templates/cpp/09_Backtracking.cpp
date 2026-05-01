/*
 * ============================================
 *  백트래킹 (Backtracking)
 * ============================================
 *  시간복잡도: 최악 O(N!), 가지치기로 단축
 *  용도: 순열, 조합, N-Queen, 부분집합
 */
#include <bits/stdc++.h>
using namespace std;

int n, m;
bool used[9];
int arr[9];

// ===== 1. 순열 (N개 중 M개 뽑기, 순서 O) =====
void permutation(int depth) {
    if (depth == m) {
        for (int i = 0; i < m; i++) cout << arr[i] << " ";
        cout << "\n";
        return;
    }
    for (int i = 1; i <= n; i++) {
        if (used[i]) continue;
        used[i] = true;
        arr[depth] = i;
        permutation(depth + 1);
        used[i] = false;            // 복원 (백트래킹 핵심!)
    }
}

// ===== 2. 조합 (N개 중 M개 뽑기, 순서 X) =====
void combination(int depth, int start) {
    if (depth == m) {
        for (int i = 0; i < m; i++) cout << arr[i] << " ";
        cout << "\n";
        return;
    }
    for (int i = start; i <= n; i++) {  // start부터 → 중복 방지
        arr[depth] = i;
        combination(depth + 1, i + 1);
    }
}

// ===== 3. 부분집합 =====
vector<int> subset;
void subsets(int idx, int n) {
    // 현재 subset 출력 (공집합 포함)
    for (int x : subset) cout << x << " ";
    cout << "\n";

    for (int i = idx; i <= n; i++) {
        subset.push_back(i);
        subsets(i + 1, n);
        subset.pop_back();          // 복원
    }
}

// ===== 4. N-Queen =====
int col[15];     // col[i] = i번 행의 퀸 열 위치
int ans_nq = 0;

bool is_safe(int row) {
    for (int i = 0; i < row; i++) {
        if (col[i] == col[row]) return false;                   // 같은 열
        if (abs(col[i] - col[row]) == abs(i - row)) return false; // 대각선
    }
    return true;
}

void nqueen(int row, int n) {
    if (row == n) { ans_nq++; return; }
    for (int c = 0; c < n; c++) {
        col[row] = c;
        if (is_safe(row)) nqueen(row + 1, n);  // 가지치기
    }
}

/*
 * 💡 핵심 암기 포인트:
 *   1. 순열: used[] 배열로 사용 여부 체크
 *   2. 조합: start 파라미터로 중복 방지
 *   3. 백트래킹 = "선택 → 재귀 → 복원"
 *   4. 가지치기(pruning): 조건 불만족 시 즉시 return
 */

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cin >> n >> m;
    // permutation(0);
    combination(0, 1);
}
