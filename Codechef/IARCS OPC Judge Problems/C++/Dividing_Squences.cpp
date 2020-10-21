/*
https://www.codechef.com/IARCSJUD/problems/DIVSEQ/
*/

#include<bits/stdc++.h>
using namespace std;
int main(){
    int n; cin>>n;
    int seq[n];
    for(int i=0;i<n;i++){
        cin>>seq[i];
    }
    int flag[n];
    flag[0]=1;
    for(int i =1;i<n;i++){
        flag[i]=1;
        for(int j=0;j<i;j++){
            if(seq[i]%seq[j]==0 && flag[j] != 0){
                flag[i]=max(flag[i],flag[j]+1);
            }
        }
    }
    cout<<*max_element(flag,flag+n);
    return 0;
}