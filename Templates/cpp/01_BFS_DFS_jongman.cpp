#include <vector>
using namespace std;

int main(void){
    vector<vector<int>> adj;
    vector<bool> visited;

    void dfs(int here){
        cout << "DFS visited " << here <<endl;
        visited[here] = true;
        for (int i = 0; i<adj[here].size(); ++i){
            int there = ad[here][i];
            if (!visited[there]){
                dfs(there)
            }
        }
    }
}