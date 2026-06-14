#include <iostream>
#include <stack>
#include <vector>

static vector<vector<int>> A;
static vector<bool> visited;
void DFS(int v);
using namespace std;

int main(void){
    ios::sync_with_stdio(false);
    cout.tie(NULL);
    cin.tie(NULL);
    int N,M;
    A.resize(N+1);
    visited = vector<bool> (N+1, false);
    
    for (int i = 0; i< M, i++){
        int s,e;
    }

    DFS(1);
    
}

void DFS(int v){
    cout << "hello word "<<endl;

}