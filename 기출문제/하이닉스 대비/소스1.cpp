#include <queue>
#include <vector>
#include <iostream>
#include <stdio.h>
//#define _CRT_SECURE_NO_WARNINGS

using namespace std;
int in[100] [100]={0,};

int dx[4] = { -1,1,0,0 };
int dy[4] = { 0,0,-1,1 };

int main(void) {
	int N, M;
	int count = 0;

	scanf("%d%d", &N, &M);
	for (int i = 0; i < N; i++) 
		for (int j = 0; j < M; j++) 
			scanf("%1d", &in[i][j]);
	
	queue<int> qx; 	queue<int> qy; queue<int> qc;
	
	qx.push(0); qy.push(0); qc.push(1);

	while (qy.empty() == false) {

		int cy = qy.front(); qy.pop();
		int cx = qx.front(); qx.pop();
		int cc = qc.front(); qc.pop();
		if (in[cx][cy] > 1) continue;
		if (cy == M - 1 && cx == N - 1) {
			count = cc;
			cout << count << "\n";
			break;
		}
		else {
			for (int l = 0; l < 4; l++) {
				int nx = cx + dx[l];
				int ny = cy + dy[l];
				if (-1 < nx && nx < N && -1 < ny && ny < M && in[nx][ny] == 1) {
					qx.push(nx); qy.push(ny); qc.push(cc + 1);
				}

				else continue;
			}
			in[cx][cy] = cc + 1;
		}
	}
	
	return 0;
}

