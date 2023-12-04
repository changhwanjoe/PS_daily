#include <string>
#include <vector>
#include<algorithm>
#include <iostream>
using namespace std;

vector<int> solution(vector<string> genres, vector<int> plays) {
	bool answer = true;
	vector<vector<string>>
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
	vector<int> res;
	vector<string> genres;
	vector<int> plays;
	genres = { "classic", "pop", "classic", "classic", "pop" };
	plays = { 500, 600, 150, 800, 2500 };
	res = solution(genres, plays);
	for (int i = 0; i < res.size(); i++) {
		cout << res[i] << "\n";
	}
	return 0;
}
