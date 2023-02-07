#include <iostream>
#include <stack>

using namespace std;

int  n, i, j;
int sum,cnt;
stack<int> s;
stack<char> oper;

int prec(char a) {
	switch (a) {
	case '(': return 1;
	case '+': return 2;
	case '*': return 3;
	}
	return 0;
}

void intopo(char* in, char* pos) {
	int end = 0;
	cnt = 0;
	for (i = 0; i < n; i++) {
		if (in[i] >= '0' && in[i] <= '9') {
			pos[end++] = in[i];
		}
		else if (in[i] == '+' || in[i] == '*') {
			while (!oper.empty() && prec(oper.top()) >= prec(in[i])) {
				pos[end++] = oper.top();
				oper.pop();
			}
			oper.push(in[i]);
		}
		else if (in[i] == '(') {
			oper.push(in[i]);
		}
		else if( in[i] ==')'){
			while (oper.top() != '(') {
				pos[end++] = oper.top();
				oper.pop();
			}
			oper.pop();
		}
	}
	while (!oper.empty()) {
		pos[end++] = oper.top();
		oper.pop();
	}
	cnt = end;
}

int postcal(char* pos) {
	sum = 0;
	int a, b;

	for (i = 0; i < cnt; i++) {
		if (pos[i] >= '0' && pos[i] <= '9') {
			s.push(pos[i] - '0');
		}
		else if (pos[i] == '+') {
			a = s.top();
			s.pop();
			b = s.top();
			s.pop();
			s.push(a + b);
		}
		else {
			a = s.top();
			s.pop();
			b = s.top();
			s.pop();
			s.push(a * b);
		}
	}
	sum = s.top();
	return sum;
}

int main() {
	int tc;
	char infix[200];
	char postfix[200];

	for (tc = 1; tc <= 10; tc++) {
		cin >> n;
		cin >> infix;

		intopo(infix, postfix);

		cout << "#" << tc << " " << postcal(postfix) << endl;

		while (!s.empty()) s.pop();
	}
}