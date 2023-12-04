//#include <bits/stdc++.h>
#include <stdio.h>
#include <queue>

using namespace std;
int N, M;
int in[100+1][100+1] = { 0, };
int visited[100+1][100+1] = { 0, };
int dx[4] = { -1,1,0,0 };
int dy[4] = { 0,0,-1,1 };

bool check(int y, int x) {
	if (y<1 || y>N || x<1 || x>M) return false;
	if (in[y][x] == 0) return false;
	if (visited[y][x])return false;

	return true;
}
int main(void) {
	scanf("%d%d", &N, &M);
	for (int i = 1; i <= N; i++)
		for (int j = 1; j <= M; j++)
			scanf("%1d", &in[i][j]);

	queue<int> qx; 	queue<int> qy; queue<int> qc;

	qx.push(1); qy.push(1); qc.push(1);
	int cnt = 0;
	while (qy.empty() == false) {

		int cy = qy.front(); qy.pop();
		int cx = qx.front(); qx.pop();
		int cc = qc.front(); qc.pop();
		if (visited[cy][cx]) continue;
		visited[cy][cx] = 1;

		if (cy == N && cx == M) {
			cnt = cc; break;
		}
		if (check(cy - 1, cx)) qy.push(cy - 1), qx.push(cx), qc.push(cc + 1);
		if (check(cy + 1, cx)) qy.push(cy + 1), qx.push(cx), qc.push(cc + 1);
		if (check(cy , cx-1)) qy.push(cy ), qx.push(cx-1), qc.push(cc + 1);
		if (check(cy , cx+1)) qy.push(cy ), qx.push(cx+1), qc.push(cc + 1);
	}
	printf("%d\n", cnt);
	return 0;
}

