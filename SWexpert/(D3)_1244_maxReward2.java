import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
 
public class Solution {
  static int[] arr, maxArr;
  static int n, swapCount, maxCount;
  static int answer;
 
  public static void main(String[] args) throws IOException {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int testCase = Integer.parseInt(br.readLine());
 
    for (int tc = 1; tc <= testCase; tc++) {
      String[] input = br.readLine().split(" ");
      swapCount = Integer.parseInt(input[1]);
      char[] tempChar = input[0].toCharArray();
      n = tempChar.length;
 
      arr = new int[n];
      maxArr = new int[n];
      for (int i = 0; i < n; i++) {
        arr[i] = tempChar[i] - 48;
      }
 
      maxCount = Integer.MIN_VALUE;
      answer = Integer.MIN_VALUE;
 
      dfs(0, 0);
 
      if (swapCount > maxCount) {
        check();
      }
 
      System.out.println("#" + tc + " " + answer);
    }
  }
 
  private static void check() {
    int remainCnt = swapCount - maxCount;
 
    // 중복 숫자 있는 경우
    for (int i = 0; i < n - 1; i++) {
      if (maxArr[i] == maxArr[i + 1]) {
        answer = getNum(maxArr);
        return;
      }
    }
 
    // 중복 숫자 없는 경우
    if (remainCnt % 2 == 0) {
      answer = getNum(maxArr);
      return;
    } else {
      swap(maxArr, n - 2, n-1);
      answer = getNum(maxArr);
      return;
    }
  }
 
  private static void dfs(int left, int cnt) throws IOException {
    maxCount = Math.max(maxCount, cnt);
     
    if (cnt == swapCount) {
      int num = getNum(arr);
      answer = Math.max(answer, num);
      return;
    }
 
 
    if (cnt == maxCount) {
      maxArr = arr.clone();
    }
 
    int max = 0;
    for (int i = left; i < n; i++) {
      if (max < arr[i]) {
        max = arr[i];
      }
    }
 
    for (int i = left; i < n; i++) {
      if (i != left && max == arr[i]) {
        swap(arr, left, i);
        dfs(left + 1, cnt + 1);
        swap(arr, i, left);
      }
 
      if (i == left && max == arr[i]) {
        dfs(left + 1, cnt);
      }
    }
  }
 
  private static int getNum(int[] arr) {
    int num = 0;
    for (int i = 0; i < n; i++) {
      num += arr[i];
      if (i != n-1) {
        num *= 10;
      }
    }
    return num;
  }
 
  static void swap(int[] arr, int i, int j) {
    int temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
  }
 
 
}
