def reverse3(nums):
    n = []
    for i in range(len(nums)-1,-1,-1):
        n.append(nums[i])
    return n