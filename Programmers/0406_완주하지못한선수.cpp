//https://school.programmers.co.kr/learn/courses/30/lessons/42576

/*
std::unordered_map 사용법 익히기.

#include <unordered_map>
std::unordered_map<string, int> d;
정의되지 않은 key에 접근하면 0을 리턴한다.
d["key"] = 0;
d["key"] = 1;

for(auto& i:d) // unordered_map의 모든 원소에 접근
cout << i.first << " " << i.second << std::endl;
*/

#include <string>
#include <vector>
#include <unordered_map>
#include <iostream>
#include <algorithm>
using namespace std;
string solution(vector<string> participant, vector<string> completion) {
    string answer = "";
    unordered_map<string, int> d;
    for(auto& i : participant) d[i]++;
    for(auto& i : completion) d[i]--;
    for(auto& i : d) {
        if (i.second >0 ){
            answer = i.first;
            break;
        }
    }
    return answer;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    cout << solution(participant, completion) << endl;
    return 0;
}
// 2025.04.06
