// TIP 
// string 들어가 있는 numbers 에 대해 
// ascii 코드는 int 이다. 
// 아스키 코드를 굳이 형변환 하지 않고 계산하는 방법. ?? -'0' 하면 int 값 나옴. 
#include <iostream>
#include <string>

using namespace std;

int main(void){
    int N = 0;
    string numbers;
    cin >> N;
    cin >> numbers;
    int sum =0;
    for (int i=0; i<numbers.length();i++){
        sum += numbers[i] -'0';
    }
    cout << sum << endl;
    return 0;

}