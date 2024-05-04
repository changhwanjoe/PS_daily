#include <string>
#include <vector>
#include <algorithm>
#include <map>
using namespace std;
bool comp(pair<string, int> a, pair<string, int> b) {
	return a.second > b.second;
}
bool comp2(pair<int, int> a, pair<int, int> b) {
	if (a.first == b.first) {
		return a.second < b.second;
	}
	return a.first > b.first;
}
vector<int> solution(vector<string> genres, vector<int> plays) {
	vector<int> answer;
	map<string, int> type;
	map<string, int>::iterator it;
	map<string, vector<pair<int, int>>> list;
	for (int i = 0; i < plays.size(); i++) {
		type[genres[i]] += plays[i];
		list[genres[i]].push_back(pair<int, int>(plays[i], i));
	}
	int i = 0;
	vector<pair<string, int>> typeName;
	for (it = type.begin(); it != type.end(); it++, i++) {
		typeName.push_back(pair<string, int>(it->first, it->second));
	}
	sort(typeName.begin(), typeName.end(), comp);

	for (int i = 0; i < typeName.size(); i++) {
		sort(list[typeName[i].first].begin(), list[typeName[i].first].end(), comp2);
		for (int j = 0; j < 2 && j < list[typeName[i].first].size(); j++) {
			answer.push_back(list[typeName[i].first][j].second);
		}
	}

	return answer;
}