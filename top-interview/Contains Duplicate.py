from typing import List

def containsDuplicate(nums: List[int]) -> bool:
    # solution 1
    # return len(set(nums)) < len(nums)

    # solution 2
    # use a set to keep existing values
    d = set()

    for x in nums:
        if x in d:
            return True
        d.add(x)
    return False 

if __name__ == '__main__':
    print(containsDuplicate([1,2,3,1]))
    print(containsDuplicate([1,2,3,4]))
    print(containsDuplicate([1,1,1,3,3,4,3,2,4,2]))