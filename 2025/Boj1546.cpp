#include <iostream>
using namespace std;

int main(void){
    int M=0;
    int N =0;
    int A[1000];

    cin >> N;
    for (int i =0; i<N; i++){
        cin >> A[i];
    }
    long sum=0;
    long max=0;
    for (int i =0; i<N; i++){
        sum+=A[i];
        if(A[i]>max){
            max=A[i];
        }
    }
    double new_average = (double)sum/max*100/N;
    cout <<new_average<<endl;
    
}