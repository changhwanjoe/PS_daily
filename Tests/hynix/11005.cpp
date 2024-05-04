#include <iostream>
#include <string>
#include <stdio.h>
#include <array>
#include <vector>

/*������ ���� N
B ���� ���
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
	int n;  //��ȯ�� 10���� ����
	cin >> n;
	//n = 60466175;
	int b;  //��ȯ�� ���̽� ����
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


