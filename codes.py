def n_sum(nums, target, n, result, results):
    if len(nums) < n or n < 2 or target < nums[0] * n or target > nums[-1] * n:
        # Early termination if not possible to achieve target
        return
    if n == 2:
        # 2-sum problem, solved using two pointers
        left, right = 0, len(nums) - 1
        while left < right:
            s = nums[left] + nums[right]
            if s == target:
                results.append(result + [nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif s < target:
                left += 1
            else:
                right -= 1
    else:
        # Recurse and reduce to (n-1)-sum problem
        for i in range(len(nums) - n + 1):
            if i == 0 or (i > 0 and nums[i - 1] != nums[i]):
                n_sum(nums[i + 1:], target - nums[i], n - 1, result + [nums[i]], results)

# Example for 4 sum problem
def four_sum(nums, target):
    nums.sort()
    results = []
    n_sum(nums, target, 4, [], results)
    return results
