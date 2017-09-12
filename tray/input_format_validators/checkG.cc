// input checker probG - ECNA2015

#include <iostream>
using namespace std;

int main(){

  int n,m;
  double x,y;

  cin>>m>>n;
	if(m<1||m>24) { cout<<"m too big"; return 1; }
if (n < 0 || n > 72) return 4;
    for (int i=0;i<n;i++){
      cin>>x>>y;
      if (x<=0.0 || x>=m || y<0.0 || y>3) {
        cout << "x y off shelf: "<<x<<" "<<y; return 2; }
    }
    cout<<endl;

return 42;
}

