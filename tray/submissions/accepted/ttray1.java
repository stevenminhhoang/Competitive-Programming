// Tom Wexler

import java.util.*;
import java.io.*;

public class ttray1 {
  public static void main(String[] args) {
        //int[][] board = new int[5][5];
    Scanner input = new Scanner(System.in);
    int m = input.nextInt();
    int n = input.nextInt();
      int[][] v = new int[m+2][3];
      for(int i = 0; i < m+2; i++) {
        v[i][0] = 1;
        v[i][1] = 1;
        v[i][2] = 1;
      }
      for(int i = 0; i < n; i++) {
        int x = (int)input.nextDouble();
        int y = (int)input.nextDouble();
        v[x+2][y] = 0;
      }
      long[][] M = new long[m+1][12];
      M[0][0] = 1;
      M[1][6] = 1;
      M[1][5] = 1;
      M[1][4] = 1;
      int i = 1;
      M[i][3] = M[i][5] + M[i-1][0]*v[i+1][0]*v[i+1][1] + M[i][9]*v[i+1][0]*v[i][0];
      M[i][2] = M[i][4] + M[i][8]*v[i+1][0]*v[i][0];
      M[i][1] = M[i][4] + M[i-1][0]*v[i+1][1]*v[i+1][2] + M[i][10]*v[i+1][1]*v[i][1];
      M[i][0] = M[i][1] + M[i][4]*v[i+1][0]*v[i+1][1] +   M[i][7]*v[i+1][0]*v[i][0];
      for(i = 2; i <= m; i++) {
        M[i][11] = M[i-1][4] + M[i-2][0]*v[i+1][2]*v[i][2];
        M[i][10] = M[i-1][2] + M[i-1][6]*v[i+1][2]*v[i][2];
        M[i][9] = M[i-1][1] + M[i-1][4]*v[i+1][1]*v[i][1];
        M[i][8] = M[i-1][1] + M[i-1][5]*v[i+1][2]*v[i][2];
        M[i][7] = M[i][8] + M[i-1][1]*v[i+1][1]*v[i+1][2] + M[i][11]*v[i+1][1]*v[i][1];
        M[i][6] = M[i-1][0] + M[i-1][1]*v[i+1][0]*v[i][0];
        M[i][5] = M[i-1][0] + M[i-1][2]*v[i+1][1]*v[i][1];
        M[i][4] = M[i-1][0] + M[i-1][3]*v[i+1][2]*v[i][2];
        M[i][3] = M[i][5] + M[i-1][0]*v[i+1][0]*v[i+1][1] + M[i][9]*v[i+1][0]*v[i][0];
        M[i][2] = M[i][4] + M[i][8]*v[i+1][0]*v[i][0];
        M[i][1] = M[i][4] + M[i-1][0]*v[i+1][1]*v[i+1][2] + M[i][10]*v[i+1][1]*v[i][1];
        M[i][0] = M[i][1] + M[i][4]*v[i+1][0]*v[i+1][1] +   M[i][7]*v[i+1][0]*v[i][0];
      }

      System.out.println(M[m][0]);
  }
}
