def missingele(nums, k):
    hashmap = {}
    for i in range(len(nums)):
        hashmap[nums[i]] = hashmap.get(nums[i], 0) + 1
    for i in range(1, nums[-1]):  
        if i not in hashmap:
            k -= 1
            if k == 0:
                return i
    return nums[-1] + k   

nums = [1, 2, 3, 4, 5]
k = 1
print(missingele(nums, k))
