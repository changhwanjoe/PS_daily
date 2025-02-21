#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <cstring>

using namespace std;

// Function prototypes
void solve();
vector<vector<int>> directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    
    int t;
    cin >> t;
    while (t--) {
        solve();
    }
    
    return 0;
}

void solve() {
    int n;
    cin >> n;
    vector<vector<int>> matrix(n, vector<int>(n));
    vector<vector<int>> dist(n, vector<int>(n, -1));
    
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cin >> matrix[i][j];
        }
    }
    
    int startX, startY, endX, endY;
    cin >> startX >> startY >> endX >> endY;
    
    queue<pair<int, int>> q;
    q.push({startX, startY});
    dist[startX][startY] = 0;
    
    while (!q.empty()) {
        auto [x, y] = q.front();
        q.pop();
        
        for (auto dir : directions) {
            int newX = x + dir[0];
            int newY = y + dir[1];
            
            if (newX >= 0 && newX < n && newY >= 0 && newY < n && matrix[newX][newY] == 0 && dist[newX][newY] == -1) {
                dist[newX][newY] = dist[x][y] + 1;
                q.push({newX, newY});
            }
        }
    }
    
    cout << dist[endX][endY] << endl;
}