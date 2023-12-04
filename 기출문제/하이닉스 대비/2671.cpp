#include <string>
#include <iostream>
#include <stdio.h>
#include <string>

/* 이 문제에서 배워야 할점 
string s;
s.substr(int a);
s.lenght();
*/
using namespace std;

bool go(string s) {
	int N = s.length();
	if (N == 0) {
		return true;
	}
	else if (N >= 4 && s[0] == '1' && s[1] == '0' && s[2] == '0') {
		int idx = 2;
		while (idx < N && s[idx] == '0') {
			idx++;
		}
		if (idx == N) return false;
		while (idx < N && s[idx] == '1') {
			idx++;
		}
		if (idx + 1 < N && s[idx] == '0' && s[idx + 1] == '0' && s[idx - 2] == '1')
		{
			return go(s.substr(idx - 1)); // s의 인덱스 idx-1 부터 끝까지 반환
		}
		else return go(s.substr(idx));
	}
	if (N >= 2 && s[0] == '0' && s[1] == '1') {
		return go(s.substr(2));
	}
	return false;
}

int main(void) {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cin >> s;
	bool ans = go(s);
	if (ans) cout << "SUBMARINE\n";
	else cout << "NOISE\n";
	return 0;

}