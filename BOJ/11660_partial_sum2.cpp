//TIP 자주 나오는 문제
// 2by 2 차원 배열의 부분합
#include <iostream>
#include <string>

using namespace std;

int main(void){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL); 
    
    int N ,M;
    int arr[100001] ={0,};
    cin >> N >> M;

    for (int i=0; i<N; i++){
        int temp = 0;
        cin >> temp;
        arr[i] = arr[i-1] + temp;
        //arr[0] = 0;
        //arr[1] = 0+temp        
    }
    for (int i=0; i<M; i++){
        int start,end;
        cin >> start >>end;
        cout << arr[end]-arr[start-1] << "\n";
    }
}