#include <iostream>
using namespace std;

bool pattern[3][20] = {{1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1},
					   {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1},
					   {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1}};
int cols = 12;

long count(int r, int c, bool fill[3][20], int cols)
{
	if (r == 3)
		return 1;
	int nextr = r;
	int nextc = c+1;
	if (nextc == cols) {
		nextc = 0;
		nextr++;
	}
	if (fill[r][c] || !pattern[r][c])
		return count(nextr, nextc, fill, cols);
	else {
		fill[r][c] = true;
		long ans = count(nextr, nextc, fill, cols);;
		if (c < cols-1 && pattern[r][c+1] && !fill[r][c+1]) {
			fill[r][c+1] = true;
			ans += count(nextr, nextc, fill, cols);
			fill[r][c+1] = false;
		}
		if (r < 2 && pattern[r+1][c] && !fill[r+1][c]) {
			fill[r+1][c] = true;
			ans += count(nextr, nextc, fill, cols);
			fill[r+1][c] = false;
		}
		fill[r][c] = false;
		return ans;
	}
}

int main()
{
	bool fill[3][20] = {0};
	for(int r=0; r<3; r++) {
		for(int c=0; c<cols; c++) {
			if (pattern[r][c])
				cout << 'X';
			else
				cout << ' ';
		}
		cout << endl;
	}
	cout << count(0, 0, fill, cols) << endl;

	return 0;
}
