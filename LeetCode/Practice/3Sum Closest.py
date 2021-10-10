#3Sum closest
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans=0
        diff=10000000
        for i in range(0,len(nums)-2):
            #print(i)
            left=i+1
            right=len(nums)-1
            while(left<right):
                #print(i,abs(target-(nums[left]+nums[right]+nums[i])))
                if(nums[left]+nums[right]+nums[i]==target):
                          return nums[left]+nums[right]+nums[i]
                if(abs(target-(nums[left]+nums[right]+nums[i]))<diff):
                            diff=abs(target-(nums[left]+nums[right]+nums[i]))
                            ans=nums[left]+nums[right]+nums[i]
                if((nums[left]+nums[right]+nums[i])>target):
                            right=right-1
                else:   left=left+1       
        return ans