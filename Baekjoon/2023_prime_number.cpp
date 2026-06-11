#include <iostream>
using namespace std;

void DFS(int number, int jaritsu);
bool isPrime(int num);
static int N;
int main(void){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> N;

    DFS(2,1);
    DFS(3,1);
    DFS(5,1);
    DFS(7,1); 
   
    return 0;
}

void DFS(int number, int jaritsu){
    if (jaritsu == N){
        if (isPrime(number)){
            cout << number << "\n";
        }
        return;
    }
    for (int i =1; i<10; i+=2){ 
        if (isPrime(number*10 + i)){              
            DFS(number*10 + i, jaritsu+1);
        }
    }
    return;
    }

bool isPrime(int num){
    for (int i =2; i<num; i++){
        if (num % i == 0){
            return false;
        }
    }
    return true;
}