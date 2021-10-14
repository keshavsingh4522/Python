#include<iostream>
using namespace std;
int knapSack(int val[], int wt[], int n, int W)
{
 int i, w;
 int V[n+1][W+1];
 int keep[n+1][W+1];
 for (w = 0; w <= W; w++)
 V[0][w]=0;
 for (i = 1; i <= n; i++)
 {
 for (w = 0; w <= W; w++)
 {
 if (wt[i-1] <= w && ( val[i-1] + V[i-1][w-wt[i-1]] > V[i-1][w] ))
 {
 V[i][w] = val[i-1] + V[i-1][w-wt[i-1]];
 keep[i][w]=1;}
 else
 V[i][w] = V[i-1][w], keep[i][w]=0;
 }
 }
 w=W;
 for(int i=n; i>0; i--)
 {
 if(keep[i][w]==1)
 {
 cout<<wt[i-1]<<' ';
 w=w-wt[i-1];
 }
 }
 cout<<endl;
 cout<< "And is equal to ";
 return V[n][W];
}
int main()
{
 int val[] = { 60, 100, 120 };
 int wt[] = { 10, 20, 30 };
 int W = 50;
 int n = sizeof(val)/sizeof(val[0]);
 cout<<"Max Profit is obtained using items "<<knapSack(val, wt, n, W)<<endl;
 return 0;
}
