#include <iostream>
#include <cmath>

using namespace std;

int main(void) {
  int w,n,i;
  double x,y;
  string line;

  cin >> w >> n;
  if (!cin)
    return 1;

  // w between 1 and 24
  if (w < 1 || w > 24)
    return 2;
  // n nonnegative
  if (n < 0)
    return 3;
  // next char is newline
  if (cin.peek() != '\n')
    return 4;

  if (n == 0) {
    getline(cin,line);
    return cin.peek() == '\n' ? 42 : 5;
  }

  for (i=0;i<n;i++) {
    cin >> x >> y;
    if (!cin)
      return 6;
    if (i < n-1 && cin.peek() == '\n')
      return 7;
    if (x == (int)x)
      return 8;
    if (y == (int)y)
      return 9;
    if (x < 0 || x >= w)
      return 10;
    if (y < 0 || y >= 3)
      return 11;
    if (x != ((int)(x*100+0.5))/100.0)
      return 12;
    if (y != ((int)(y*100+0.5))/100.0)
      return 13;
  }

  // we win!
  return 42;
}

