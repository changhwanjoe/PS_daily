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
		if (sum == N) { // sum 이랑 같으면 sum< N 과같이 맨뒤자리추가, 갯수 추가 
			count ++;
			end_index++;
			sum += end_index;
		}
		else if (sum > N) { //sum 이 N보다 크면 맨 앞자리 뺌
			sum -= start_index;
			start_index++;
		}
		else if (sum < N) { // sum 이 N 보다 작으면 뒤 포인터 하나 늘림 (맨뒷자리 추가)
			end_index++;
			sum += end_index;

		}
	}
	cout << count << endl;
	return 0;
}