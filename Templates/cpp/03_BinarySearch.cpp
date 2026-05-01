/*
 * ============================================
 *  이분 탐색 (Binary Search)
 * ============================================
 *  시간복잡도: O(log N)
 *
 *  1. 기본 이분 탐색: 특정 값 찾기
 *  2. Lower Bound: target 이상인 첫 위치
 *  3. Upper Bound: target 초과인 첫 위치
 *  4. Parametric Search: 조건을 만족하는 최솟값/최댓값
 */
#include <bits/stdc++.h>
using namespace std;

// ===== 1. 기본 이분 탐색 =====
int binary_search(vector<int>& arr, int target) {
    int lo = 0, hi = arr.size() - 1;

    while (lo <= hi) {
        int mid = lo + (hi - lo) / 2;      // 오버플로 방지
        if (arr[mid] == target) return mid;
        else if (arr[mid] < target) lo = mid + 1;
        else hi = mid - 1;
    }

    return -1;  // 못 찾음
}

// ===== 2. Lower Bound (직접 구현) =====
// target 이상인 첫 번째 위치 반환
int lower_bound_manual(vector<int>& arr, int target) {
    int lo = 0, hi = arr.size();

    while (lo < hi) {              // 주의: lo <= hi 가 아님!
        int mid = lo + (hi - lo) / 2;
        if (arr[mid] < target) lo = mid + 1;
        else hi = mid;             // target 이상이면 hi를 줄임
    }

    return lo;
}

// ===== 3. Parametric Search =====
// "조건을 만족하는 최솟값 찾기" 패턴
//   - check(x): x가 조건을 만족하면 true
//   - lo: 무조건 false, hi: 무조건 true
int parametric_search() {
    int lo = 0, hi = 1e9;  // 답의 범위

    while (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        if (/* check(mid) */ true) {
            hi = mid;       // 조건 만족 → 더 작은 값 시도
        } else {
            lo = mid + 1;   // 조건 불만족 → 더 큰 값 시도
        }
    }

    return lo;  // 조건을 만족하는 최솟값
}

/*
 * 💡 핵심 암기 포인트:
 *   1. mid = lo + (hi - lo) / 2  (오버플로 방지)
 *   2. 기본 탐색: lo <= hi, return mid
 *   3. Lower bound: lo < hi, hi = mid (lo == hi 될 때까지)
 *   4. STL: lower_bound(begin, end, val) — 이상
 *           upper_bound(begin, end, val) — 초과
 *   5. Parametric Search: 결정 문제로 바꿔서 이분 탐색
 */

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    vector<int> arr = {1, 3, 5, 7, 9, 11};

    // 기본 이분 탐색
    cout << binary_search(arr, 7) << "\n";     // 3

    // STL lower_bound / upper_bound
    auto it = lower_bound(arr.begin(), arr.end(), 5);
    cout << (it - arr.begin()) << "\n";         // 2 (인덱스)

    return 0;
}
