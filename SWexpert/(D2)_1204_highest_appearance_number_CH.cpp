#include <iostream> 

using namespace std;

int main(void)
{
    int T = 0;
    int t = 0;

    cin >> T;
    for (int i = 0; i < T; i++) {
        cin >> t;

        int score[101] = {0,};
        int temp_score = 0;
        int num_of_score = 0;
        int highes_score = 0;
        int result = 0;

        for (int j = 0; j < 1000; j++) {
            cin >> temp_score;
            score[(temp_score)] += 1;

        }
        for (int k = 100; k >= 0; k--) {
            if (score[k] > num_of_score) {
                num_of_score = score[k];
                result = k;
            }
        }
        cout << "#" << t << " " << result<<endl;

    }
}