#include<iostream>
#define n 5
#define INFY 99999
using namespace std;
void print(int A[n][n]);
void APSP(int cost[n][n]) {
 int A[n][n], i, j, k;
 for (i = 0; i < n; i++) {
 for (j = 0; j < n; j++) {
 A[i][j] = cost[i][j];
 }
 }
 for (k = 0; k < n; k++) {
 for (i = 0; i < n; i++) {
 for (j = 0; j < n; j++) {
 if (A[i][k] + A[k][j] < A[i][j])
 A[i][j] = A[i][k] + A[k][j];
 }
 }
 }
 print(A);
}
void print(int A[n][n]) {
 cout<<"shortest distance between every pair of vertices: \n";
 for (int i = 0; i < n; i++) {
 for (int j = 0; j < n; j++) {
 if (A[i][j] == INFY)
 cout<<" INFY ";
 else
 cout<<" "<<A[i][j]<<" ";
 }
 cout<<endl;
 }
}
int main() {
 int cost[n][n] = { {0,10,50,65,INFY},
 {INFY,0,30,INFY,4},
 {INFY,INFY,0,20,44},
 {INFY,70,INFY,0,23},
 {6,INFY,INFY,INFY,0}
 };
 APSP(cost);
 return 0;
}
