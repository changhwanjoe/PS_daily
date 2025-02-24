#include <vector>
#include <iostream>
using namespace std;

class Solution{
public:
    
}


int main() {

	vector<int> A; // 선언
	A.push_back(1);
	A.insert(A.begin(), 7); // 맨 앞에 7을 추가
    A.erase(A.begin()+3); //index 3 원소 삭제
    A.clear(); //모든 원소 삭제 

	for (int i : A) {
		std::cout << i << " ";
	}
	return 0;
}
