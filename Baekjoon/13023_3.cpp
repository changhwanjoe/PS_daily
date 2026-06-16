#include <iostream>
#include <vector>

using namespace std;

static vector<vector<int>> A;
static vector<bool> visited;
<<<<<<< HEAD:Baekjoon/13023.cpp
static bool arrived;
void DFS(int i, int depth);
int main(void)
{
=======
void DFS(int number, int depth);
void DFS(int number, int depth){
    if (depth == 5){
        cout << 1 << "\n";
        return;
    }
    for (int i=0; i<friend_list.size(); i++){
        
    }
})
int main(void){
>>>>>>> bbfdc3e (0615):Baekjoon/13023_2.cpp
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N, M;
    cin >> N >> M;

    A.resize(N);
    visited.resize(N, false);

    for (int i =0; i<M; i++)
    {
        int a, b;
        cin >> a >> b;
        A[a].push_back(b);
        A[b].push_back(a);
    }
    arrived = false;

    for (int i=0; i<N; i++)
    {
        DFS(i,1);
        if (arrived)
        {
            break;
        }
    }
    if (arrived)
    {
        cout << 1 <<endl;
    }
    else 
    {
        cout <<0 <<endl;
    }

    return 0;
}

void DFS(int i, int depth){
    if (depth >=5 || arrived){
        arrived = true;
        return;
    }
    visited[i] = true;

    for (const int node : A[i])
    {
        if (!visited[node])
        {
            DFS(node,depth +1);
        }
    }
    }
