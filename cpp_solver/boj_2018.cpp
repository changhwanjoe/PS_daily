#include <iostream>

using namespace std;

int main(void) {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);

	int N; //15
	cin >> N;
	int count = 1;
	int sum = 1;
	int start_index = 1;
	int end_index = 1;

	while (end_index != N) {
		if (sum == N) { // sum �̶� ������ sum< N ������ �ǵ��ڸ��߰�, ���� �߰� 
			count ++;
			end_index++;
			sum += end_index;
		}
		else if (sum > N) { //sum �� N���� ũ�� �� ���ڸ� ��
			sum -= start_index;
			start_index++;
		}
		else if (sum < N) { // sum �� N ���� ������ �� ������ �ϳ� �ø� (�ǵ��ڸ� �߰�)
			end_index++;
			sum += end_index;

		}
	}
	cout << count << endl;
	return 0;
}