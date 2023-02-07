#include <iostream> 
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>

using namespace std;

int main(void)
{
    vector <int> v(8);
    int N = 0;
    int K[50][9] = { 0, };
    int arr[9] = { 0, };

    int runner = 0;

    bool gameend = false;
    int highest_score = 0;

    int permuqueue[8] = { 0, };
    v = { 1,2,3,4,5,6,7,8 };

    cin >> N;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < 9; j++) {
            cin >> K[i][j];
        }
    }
    cout << "input complete" << endl;

    do {
        int inning = 0;
        int battingqueue[9] = { 0, };
        int outcount = 0;
        int score = 0;
        int index = 0;
        int batting_index = index % 9;

        while (inning < N) {
            battingqueue[3] = K[inning][0];
            for (int i = 0; i < 3; i++) {
                battingqueue[i] = K[inning][v[i]];
            }
            for (int i = 4; i < 9; i++) {
                battingqueue[i] = K[inning][v[i - 1]];
            }

            int base[3] = { 0, };//initialize q to 0000
            //for (int j = 1; j < 9; j++) {
            //    permuqueue[j] = K[inning][j]; // k[2,3,4,5,6,7,8,9]
            //}

            while (1) {
                if (battingqueue[batting_index] == 0) {
                    outcount++;
                    if (outcount >= 3) {
                        inning++;
                        outcount = 0;
                        break;
                    }
                }
                else if (battingqueue[batting_index] == 1) {
                    if (base[2] == 1) {
                        score++;
                    }
                    for (int i = 2; i > 0; i--) {
                        base[i] = base[i - 1];
                    }
                    base[0] = 1;
                }
                else if (battingqueue[batting_index] == 2) {
                    score += base[2] + base[1];
                    base[2] = base[0];
                    base[1] = 1;
                    base[0] = 0;
                }
                else if (battingqueue[batting_index] == 3) {
                    score += base[2] + base[1] + base[0];
                    base[2] = 1;
                    base[1] = 0;
                    base[0] = 0;
                }
                else if (battingqueue[batting_index] == 4) {
                    score += base[2] + base[1] + base[0] + 1;
                    base[0] = 0;
                    base[1] = 0;
                    base[2] = 0;
                }
                index++;
            }
        }
        if (highest_score <= score) {
            highest_score = score;
        }

    } while (next_permutation(v.begin(), v.end()));
    cout << highest_score << endl;

    return 0;
}