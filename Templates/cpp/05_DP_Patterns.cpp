/*
 * ============================================
 *  동적 프로그래밍 (Dynamic Programming) 패턴 모음
 * ============================================
 *  핵심: 점화식 세우기 → 메모이제이션 or 반복문
 *
 *  1. 1차원 DP (피보나치, 1로 만들기)
 *  2. 2차원 DP (배낭, LCS)
 *  3. LIS (최장 증가 부분 수열)
 */
#include <bits/stdc++.h>
using namespace std;

// ===== 1. 1로 만들기 (BOJ 1463) =====
// dp[i] = i를 1로 만드는 최소 연산 횟수
void make_one() {
    int n;
    cin >> n;
    vector<int> dp(n + 1, 0);

    for (int i = 2; i <= n; i++) {
        dp[i] = dp[i - 1] + 1;                     // -1
        if (i % 2 == 0) dp[i] = min(dp[i], dp[i / 2] + 1);  // /2
        if (i % 3 == 0) dp[i] = min(dp[i], dp[i / 3] + 1);  // /3
    }

    cout << dp[n] << "\n";
}

// ===== 2. 0/1 배낭 (Knapsack) =====
// dp[i][w] = i번째 물건까지 고려, 무게 w일 때 최대 가치
void knapsack() {
    int n, W;
    cin >> n >> W;
    vector<int> w(n + 1), v(n + 1);
    for (int i = 1; i <= n; i++) cin >> w[i] >> v[i];

    vector<vector<int>> dp(n + 1, vector<int>(W + 1, 0));

    for (int i = 1; i <= n; i++) {
        for (int j = 0; j <= W; j++) {
            dp[i][j] = dp[i - 1][j];               // i번째 물건 안 넣음
            if (j >= w[i]) {
                dp[i][j] = max(dp[i][j], dp[i - 1][j - w[i]] + v[i]);  // 넣음
            }
        }
    }

    cout << dp[n][W] << "\n";
}

// ===== 3. LCS (최장 공통 부분 수열) =====
// dp[i][j] = A[0..i-1]과 B[0..j-1]의 LCS 길이
void lcs() {
    string a, b;
    cin >> a >> b;
    int n = a.size(), m = b.size();
    vector<vector<int>> dp(n + 1, vector<int>(m + 1, 0));

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            if (a[i - 1] == b[j - 1]) {
                dp[i][j] = dp[i - 1][j - 1] + 1;
            } else {
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);
            }
        }
    }

    cout << dp[n][m] << "\n";
}

// ===== 4. LIS (최장 증가 부분 수열) — O(N log N) =====
void lis() {
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int& x : arr) cin >> x;

    vector<int> dp;     // dp[i] = 길이 i+1인 증가 수열의 마지막 원소 최솟값

    for (int x : arr) {
        auto it = lower_bound(dp.begin(), dp.end(), x);
        if (it == dp.end()) {
            dp.push_back(x);       // 뒤에 추가 (수열 길이 증가)
        } else {
            *it = x;               // 기존 값을 더 작은 값으로 교체
        }
    }

    cout << dp.size() << "\n";      // LIS 길이
}

/*
 * 💡 핵심 암기 포인트:
 *   1. DP = "큰 문제를 작은 문제로" + "중복 계산 제거"
 *   2. 점화식 패턴:
 *      - dp[i] = dp[i-1] + ... (1차원)
 *      - dp[i][j] = max(dp[i-1][j], dp[i][j-1]) (2차원)
 *   3. 배낭: "넣는다 vs 안 넣는다" 선택
 *   4. LIS: lower_bound로 O(N²) → O(N log N)
 *   5. 초기값 설정이 가장 중요!
 */

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    // 원하는 함수 호출
    // make_one();
    // knapsack();
    // lcs();
    lis();

    return 0;
}
