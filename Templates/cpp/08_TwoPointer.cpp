/*
 * ============================================
 *  투 포인터 & 슬라이딩 윈도우
 * ============================================
 *  시간복잡도: O(N)
 *  용도: 연속 부분 배열, 구간 합, 특정 조건 구간
 */
#include <bits/stdc++.h>
using namespace std;

// ===== 1. 투 포인터: 합이 S 이상인 최소 구간 =====
int min_subarray_len(vector<int>& arr, int S) {
    int n = arr.size();
    int lo = 0, sum = 0, ans = INT_MAX;

    for (int hi = 0; hi < n; hi++) {
        sum += arr[hi];
        while (sum >= S) {
            ans = min(ans, hi - lo + 1);
            sum -= arr[lo++];
        }
    }
    return ans == INT_MAX ? 0 : ans;
}

// ===== 2. 투 포인터: 정렬된 배열에서 합이 target인 쌍 =====
pair<int,int> two_sum_sorted(vector<int>& arr, int target) {
    int lo = 0, hi = arr.size() - 1;
    while (lo < hi) {
        int sum = arr[lo] + arr[hi];
        if (sum == target) return {lo, hi};
        else if (sum < target) lo++;
        else hi--;
    }
    return {-1, -1};
}

// ===== 3. 슬라이딩 윈도우: 고정 크기 K 구간 최대합 =====
int max_sum_window(vector<int>& arr, int k) {
    int n = arr.size();
    int sum = 0;
    for (int i = 0; i < k; i++) sum += arr[i];

    int ans = sum;
    for (int i = k; i < n; i++) {
        sum += arr[i] - arr[i - k];     // 오른쪽 추가, 왼쪽 제거
        ans = max(ans, sum);
    }
    return ans;
}

/*
 * 💡 핵심 암기 포인트:
 *   1. 투 포인터: lo, hi 두 포인터가 같은 방향 or 양 끝에서 이동
 *   2. 슬라이딩 윈도우: 고정 크기 구간을 한 칸씩 밀기
 *   3. while(sum >= S) → 조건 만족하면 lo를 줄여서 최소 구간 찾기
 *   4. 정렬된 배열 + 두 수의 합 → 양쪽에서 좁히기
 */

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    return 0;
}
