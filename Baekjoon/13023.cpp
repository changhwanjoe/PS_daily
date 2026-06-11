#include <iostream>

#include <vector>
using namespace std;

static vector<vector<int>> friend_list;
static vector<bool> visited;
int main(void){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    int N, M;
    cin >> N >> M;
    friend_list.resize(N);
    visited.resize(N+1, false);
    for (int i =0; i<M; i++){
        int a, b;
        cin >> a >> b;
        friend_list[a].push_back(b);
        friend_list[b].push_back(a);
    }   

    return 0;
}
