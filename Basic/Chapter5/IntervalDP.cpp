#include <iostream>

using namespace std;

const int N = 310;
int n, s[N], f[N][N];

int main() {
  cin >> n;
  for (int i = 1; i <= n; ++i) {
    int x;
    cin >> x;
    s[i] = s[i - 1] + x;
  }

  for (int interval = 2; interval <= n; ++interval) {
    for (int i = 0; i + interval <= n; ++i) {
      int l = i, r = i + interval - 1;
      f[l][r] = 1e9;
      for (int k = l; k < r; ++k) {
        f[l][r] = min(f[l][r], f[l][k] + f[k + 1][r] + s[r + 1] - s[l]);
      }
    }
  }

  cout << f[0][n - 1];
  return 0;
}