#include <iostream>
#include <stack>
#include <vector>
using namespace std;

static vector<vector <int>> A;
static vector<bool> visited;

void DFS(int v);
int main (void) {

	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int N, M;
	N = 6;
	M = 5;
	//cin >> N >> M;
	A.resize(N + 1);
	visited = vector<bool>(N + 1, false);

	vector<int> s= { 1,2,5,3,4 };
	vector<int> e = { 2,5,1,4,6 };
	for (int i = 0; i < s.size();i++) {
		
		A[s[i]].push_back(e[i]);
		A[e[i]].push_back(s[i]);
	}

	

	//for (int i = 0; i < M; i++) {
	//	int s, e;
	//	cin >> s >> e;
	//	A[s].push_back(e);
	//	A[e].push_back(s);
	//}

	int count = 0;
	for (int i = 0; i < N + 1; i++) {
		if (!visited[i]) {
			count++;
			DFS(i);
		}
	}
	cout << count << "\n";
}

void DFS(int v) {
	if (visited[v]) {
		return;
	}
	
	visited[v] = true;

	for (int i : A[v]) {
		if (visited[i] == false) {
			DFS(i);
		}
	}
}

