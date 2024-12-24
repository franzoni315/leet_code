from typing import List


def removeDuplicates(nums: List[int]) -> int:
    # out = []
    # loop 1. x = 1 -> out = [1]
    # loop 2. x = 1 -> out = [1]
    # loop 3. x = 2 -> out = [1, 2]

    n = 0
    for x in nums:
        if n == 0 or nums[n - 1] < x:
            nums[n] = x
            n += 1
    
    print(nums)
    return n


if __name__ == '__main__':
    print(removeDuplicates([1,1,2]))
    print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))