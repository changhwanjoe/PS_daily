#include<iostream>
#include<vector>
using namespace std;

int main(void) {
	int n;  //��ȯ�� 10���� ����
	//cin >> n;

	n = 60466175;
	int b;  //��ȯ�� ���̽� ����
	//cin >> b;
	b = 36;

	vector<int> v;

	while (1) {
		v.push_back(n%b);   //�ش� ������ ���� �������� vector�� ����
		n /= b;
		if (n == 0) break;
	}

	vector<int>::reverse_iterator iter;
	for (iter = v.rbegin(); iter != v.rend(); iter++) {
		if (*iter >= 10) {
			char c = *iter - 10 + 'A';  //10 �̻��� ���ĺ��� char Ÿ������ ���
			cout << c;
		}
		else {
			cout << *iter;          //10 �̸��� ���� int Ÿ������ ���
		}
	}

	return 0;
}

