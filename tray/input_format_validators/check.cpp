#include <iostream>
#include <cmath>
#include <cstdio>
using namespace std;

const int MAXM = 24;

double xs[5000], ys[5000];

bool repeat(int n)
{
	for(int i=0; i<n; i++) {
		if (xs[i] == xs[n] && ys[i] == ys[n])
			return true;
	}
	return false;
}

int main()
{
	int n, m, s, t;
	double x, y;

	cin >> m >> n;
		if (m < 1 || m > MAXM) {
			cout << "ERROR: invalid m " << m << endl; return 1; }
		if (n < 0 || n > 72) {
			cout << "ERROR: invalid n " << n << endl; return 2; }
		for(int i=0; i<n; i++) {
			cin >> x >> y;
			if (x < 0 || x > m || (x - (int)x == 0)) {
				cout << "ERROR: invalid x " << x << " in line " << i << endl; return 3;}
			if (y < 0 || y > 3 || (y - (int)y == 0)) {
				cout << "ERROR: invalid y " << y << " in line " << i << endl; return 4; }
			xs[i] = x, ys[i] = y;
			if (repeat(i)) {
				cout << "ERROR: repeat point " << x << ',' << y << " in line " << i << endl; return 5; }
		}
return 42;
}

