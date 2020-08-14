#include<iostream>
#include<queue>
using namespace std;
# define ug unsigned long long
int main()
{
    ug n,k,v,sum=0;
    priority_queue <int> q;
    cin>>n>>k;
    while(n--)
    {
        cin>>v;
        sum+=v;
        q.push(v);
    }
    while(k--)
    {
        v=q.top();
        q.pop();
        q.push(v/2);
        sum-=(v-v/2);
    }
    cout<<sum;
    return 0;
}