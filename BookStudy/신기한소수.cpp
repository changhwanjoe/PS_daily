//https://www.acmicpc.net/source/92538660

#include <iostream>
#include <vector>
using namespace std;

void dfs(int v, int jarisu);

bool isPrime(int v);
static int N;

int main(void)
{

    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> N;

    dfs(2, 1);
    dfs(3, 1);
    dfs(5, 1);
    dfs(7, 1);

    return 0;
}

void dfs(int v, int jarisu)
{
    if (jarisu == N)
    {
        if (isPrime(v))
        {
            cout << v << "\n";
        }
        return;
    }

    int new_v;
    for (int i = 1; i <= 9; i = i + 2)
    {
        new_v = v * 10 + i;
        if (isPrime(new_v))
        {
            dfs(new_v, jarisu+1);
        }
    }
}

bool isPrime(int v)
{
    for (int i = 2; i <= v/2; i++)
    {
        if (v % i == 0)
            return false;
    }
    return true;
}