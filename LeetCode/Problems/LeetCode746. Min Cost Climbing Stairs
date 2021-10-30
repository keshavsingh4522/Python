class Solution {
public:
    int dp[1001];
    int costcalc(int i,vector<int>& cost)
    {
        if(i>=cost.size())
            return 0;
        if(dp[i]!=-1)
            return dp[i];
        int op1=cost[i]+costcalc(i+1,cost);
        int op2=cost[i]+costcalc(i+2,cost);
        return dp[i]=min(op1,op2);
    }
    int minCostClimbingStairs(vector<int>& cost) {
        memset(dp,-1,sizeof dp);
        return(min(costcalc(0,cost),costcalc(1,cost)));
    }
};
