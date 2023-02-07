#include <string>
#include <vector>
#include<algorithm>
#include <iostream>
using namespace std;

bool solution(vector<string> phone_book) {
	bool answer = true;
	string temp;
	string temp2;
	sort(phone_book.begin(), phone_book.end());
	for (int i = 0; i < phone_book.size(); i++) {
		temp = phone_book[i];
		for (int j = i + 1; j < phone_book.size(); j++) {
			temp2 = phone_book[j];
			if (temp == temp2.substr(0, temp.size())) {
				answer = false;
				break;
			}
		}
		if (answer == false) break;
	}

	return answer;
}

int main(void) {
	bool res;
	vector<string> phone_book;
	phone_book = {"119", "97674223", "1195524421" };
	res = solution(phone_book);
	cout << res;
	return 0;
}
