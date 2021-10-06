def lengthOfLongestInceasingSubsequence(nums):
    nums_len = len(nums)
    dp = [1] * nums_len

    for i in range(1, nums_len):
        for j in range(0, i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


if __name__ == '__main__':
    nums = []
    n = int(input())
    for _ in range(0, n):
        ele = int(input())
        nums.append(ele)
    print(nums)
    print(lengthOfLongestInceasingSubsequence(nums))
