#include <vector>
#include <iostream>
#include <d
using namespace std;
static vector<vector<int>> A;
static vector<int> visited_DFS;

void BFS(int v);
void DFS(int v);

int main(void){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N,M,V;
    cin >> N >> M >> V;
    A.resize(N+1);
    visited_DFS.resize(N+1,false);

    for (int i =0; i<M; i++){
        int a,b;
        cin >> a>>b;
        A[a].push_back(b);
        A[b].push_back(a);
    }
    DFS(V);
    BFS(V);
    return 0;
}
void DFS(int v){
    visited_DFS[v] = true;
    cout << v ;
    for (int i : A[v]){
        if (!visited_DFS[i]){
            DFS(i);
        }
    }
    
}
void BFS(int v){
    cout << "RUN BFS"<<endl;
}
