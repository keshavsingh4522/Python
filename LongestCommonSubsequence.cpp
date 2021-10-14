#include<iostream>
#include<string.h>
using namespace std;
int i,j,m,n,c[20][20];
char x[20],y[20],b[20][20];
void print_lcs(int i,int j)
{
 if(i==0 || j==0)
 return;
 if(b[i][j]=='d')
 {
 print_lcs(i-1,j-1);
 cout<< x[i-1];
 }
 else if(b[i][j]=='u')
 print_lcs(i-1,j);
 else
 print_lcs(i,j-1);
}
void lcs_length()
{
 m=strlen(x);
 n=strlen(y);
 for(i=0; i<=m; i++)
 c[i][0]=0;
 for(i=0; i<=n; i++)
 c[0][i]=0;
 for(i=1; i<=m; i++)
 for(j=1; j<=n; j++)
 {
 if(x[i-1]==y[j-1])
 {
 c[i][j]=c[i-1][j-1]+1;
 b[i][j]='d'; //diagonal
 }
 else if(c[i-1][j]>=c[i][j-1])
 {
 c[i][j]=c[i-1][j];
 b[i][j]='u'; //vertical
 }
 else
 {
 c[i][j]=c[i][j-1];
 b[i][j]='l'; //horizontal
 }
 }
}
int main()
{
 cout<<"Enter 1st sequence: ";
 cin>>x;
 cout<<"Enter 2nd sequence: ";
 cin>>y;
 cout<<"\nThe Longest Common Subsequence is: ";
 lcs_length();
 print_lcs(m,n);
 cout<<endl;
 return 0;
}
