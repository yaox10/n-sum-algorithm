# The function signature now includes 'start' to avoid slicing
def n_sum_optimized(nums, target, n, start, result, results):
    # Early termination check remains the same
    if len(nums) - start < n or n < 2 or target < nums[start] * n or target > nums[-1] * n:
        return

    # Base case (2-sum) is modified to use the 'start' index
    if n == 2:
        left, right = start, len(nums) - 1
        while left < right:
            s = nums[left] + nums[right]
            if s == target:
                # OPTIMIZATION 2: Use the existing result list and create a copy only for the final answer
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
        # The loop now starts from the 'start' index
        for i in range(start, len(nums) - n + 1):
            # Duplicate check is slightly adjusted for the 'start' index
            if i == start or nums[i - 1] != nums[i]:
                # OPTIMIZATION 2: Append and pop for backtracking
                result.append(nums[i])
                # OPTIMIZATION 1: Pass 'i + 1' instead of slicing the array
                n_sum_optimized(nums, target - nums[i], n - 1, i + 1, result, results)
                result.pop() # Backtrack

# The wrapper function is updated to call the optimized version
def four_sum_optimized(nums, target):
    nums.sort()
    results = []
    # Initial call starts at index 0 with an empty result list
    n_sum_optimized(nums, target, 4, 0, [], results)
    return results

# --- Example Usage ---
nums_list = [1, 0, -1, 0, -2, 2]
target_sum = 0
print(four_sum_optimized(nums_list, target_sum))
# Output: [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]