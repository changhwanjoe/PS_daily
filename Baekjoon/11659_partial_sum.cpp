//ERROR 
// 맨 마지막 줄에 endl; 쓰면 안되고 "\n"; 써야됨.. 이유는 모름 

//TIP : 
//구간 합은 자주 쓰이는 알고리즘이다 꼭 알아둘것. 
// S[i] = S[i-1] + A[i]
// S[j] - S[i-1] = i에서 j까지 구간합

//Tip 2 
//ios::sync_with_stdio(false);
//cin.tie(NULL);
//cout.tie(NULL); 
// 세줄 추가할것

//Tip3 . N M 연속적으로 input 받을때 cin >> a >> b; 

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

    for (int i=1; i<=N; i++){
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