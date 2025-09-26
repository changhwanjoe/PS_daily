//https://school.programmers.co.kr/learn/courses/30/lessons/159993
//미로탈출

#include <queue>
#include <string>
#include <vector>

using namespace std;

struct Point{
    int y;
    int x;
    int cnt;
};

int dy[4] = {-1,0,1,0};  //상 좌 하 우
int dx[4] = {0,-1,0,1}; 
int n,m;

//현재 좌표가 유효한 좌표인지 확인
bool isWithinRange(int x, int y){return 0<=y && y<n && 0<=x && x<m;}

Point findStartPoint(char start, vector<string> &maps) {
    for (int i =0; i<n; i++){
        for (int j =0; j<m;j++){
            if (maps[i][j]==start){
                return {i,j,0};
            }
        }
    }
    return {-1,-1,-1}; // 시작점을 찾지 못한 경우, y,x,cntr
}

int bfs(char start, char end, vector<string> &maps){
    bool visited[101][101] = {false};
    queue<Point> q;
    q.push(findStartPoint(start, maps));

    while (!q.empty()){
        Point current = q.front();
        q.pop();

        if (maps[current.y][current.y]==end){
            return current.cnt;
        }
        for( int i=0;i<4; i++)
        {
            int ny = current.y+dy[i];
            int nx = current.x + dx[i];
            if (isWithinRange(ny,nx) && !visited[ny][nx] &&maps[ny][nx]!='X'){
                q.push({ny,nx,current.cnt+1});
                visited[ny][nx] = true;
            } 
        }
    }
    return -1;
}


using namespace std;

int solution(vector<string> maps) {
    int answer = 0;
    n = maps.size();
    m = maps[0].size();

    int distanceToL = bfs('S','L',maps);
    if (distanceToL == -1){
        return -1;
    }
    int distanceTOE = bfs('L','E',maps);
    return distanceTOE == -1 ? -1 : distanceToL + distanceTOE;
}