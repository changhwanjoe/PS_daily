#include <iostream>
#include <string>
#include <stdio.h>
#include <array>
#include <vector>

/*십진법 진수 N
B 진법 출력
*/
using namespace std;
vector<int> v;

void recursive_(int n, int b) {
	int c = 0;
	int d = 0;
	int temp = 0;
	
	if (n == 0) {
		return ;
	}
	else {
		temp = n / b;
		d = n % b;
		v.push_back(d);
		recursive_(temp, b);
		return;
	}
}

int main(void)
{
	int n;  //변환할 10진수 숫자
	cin >> n;
	//n = 60466175;
	int b;  //반환할 베이스 진수
	cin >> b;
	//b = 36;
	recursive_(n, b);

	vector<int>::reverse_iterator iter;
	for (iter = v.rbegin(); iter != v.rend(); iter++) {
		if (*iter >= 10) {
			char alpha = *iter - 10 + 'A';
			cout << alpha;
		}
		else {
			cout << *iter;
		}
	}
}


