#include <queue>
#include <stdio.h>
#include <memory.h>
using namespace std;

struct Node {
	int x;
	int y;
	Node(int _x, int _y) {
		x = _x;
		y = _y;
	}
};
void bfs() {
	queue<Node> q;
	q.push(Node(0, 0));
	visited[0][0] = true;
	int dx[] = { 1,-1,0,0 };
	int dy[] = { 0,0,1,-1 };
	while (!q.empty()) {
		int x = q.front().x;
		int y = q.front().y;
		q.pop();
		for (int i = 0; i < 4; i++) {
			int ax = x + dx[i];
			int ay = y + dy[i];
			if (ax >= 0 && ay >= 0 && ax < n && ay < n) {
				if (!visited[ax][ay] || d[ax][ay] > d[x][y] + map[ax][ay]) {
					d[ax][ay] = d[x][y] + map[ax][ay];
					q.push(Node(ax, ay));
					visited[ax][ay] = true;
				}
			}
		}
	}
}