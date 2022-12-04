'''
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

pre =  [1, 2, 6, 24]
post = [1, 24, 12, 4]
res = [24, 12, 8, 6]
'''


class Solution:
    def productExceptSelf(self, nums):
        pre = []
        post = []

        multiplier = 1
        for num in nums:
            acum = multiplier * num
            multiplier = acum
            pre.append(acum)

        multiplier = 1
        for num in reversed(nums):
            acum = multiplier * num
            multiplier = acum
            post.append(acum)

        post.reverse()

        ans = []
        for i in range(len(nums)):
            pre_num = pre[i - 1] if i - 1 >= 0 else 1
            post_num = post[i + 1] if i + 1 < len(post) else 1
            ans.append(pre_num * post_num)

        return ans
