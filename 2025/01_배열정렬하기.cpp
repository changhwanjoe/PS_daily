//배열 정렬하기
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> arr ={-1,5,2,4,3};
vector<int> solution(vector<int> arr){
    sort(arr.begin(), arr.end());
    return arr;   
}
int main(void){
    vector<int> answer;
    answer =solution(arr);
    for (auto i :answer){
        cout <<i <<endl;
    }

}