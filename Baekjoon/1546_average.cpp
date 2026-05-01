//TIP : 
//line 25 
//배열을 통째로 계산 할 수 있음. 배열 하나하나 iteration 안해도됨. 
// (A /max *100 + B/max*100)2 =(a+b)/max*100/2

#include <iostream>
#include <string>

using namespace std;

int main(void){
    int N = 0;
    int A[1000];
    cin >> N;

    for (int i=0; i<N; i++){
        cin >> A[i];
    }

    long sum = 0;
    long max = 0;

    for (int i=0; i<N; i++){
        if (A[i] >max){
            max = A[i];
        }
        sum = sum+A[i];

    }
    //배열을 통째로 계산 할 수 있음. 배열 하나하나 iteration 안해도됨. 
    // (A /max *100 + B/max*100)2 =(a+b)/max*100/2
    double result =sum * 100.0 /max / N;
    cout << result << endl;
    return 0;

}