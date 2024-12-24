from typing import List

def rotate(nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    # the position of each element must increase by k
    # if k is greater than len, then take the mod
    # Ex: nums = [1,2,3,4,5,6,7], k = 3
    # set rotate_pos = 0
    # 1 should go to position 3, and save mem = 4 => nums = [1,2,3,1,5,6,7], rotate_pos = 3
    # 4 should go to position 6, and save mem = 7 => nums = [1,2,3,1,5,6,4], rotate_pos = 6
    # 7 should go to position 2, and save mem = 3 => nums = [1,2,7,1,5,6,4], rotate_pos = 2
    # ...

    # if k == 0:
    #     return

    # n = len(nums)
    # rotate_pos = 0

    # contains_cycle = False
    # cycle_length = 0
    # if n % k == 0:
    #     contains_cycle = True
    #     cycle_length = n / k

    # mem = nums[0]
    # cycle_counter = cycle_length
    # for i in range(n):
    #     if contains_cycle and cycle_counter == 0:
    #         rotate_pos += 1
    #         mem = nums[rotate_pos]
    #         cycle_counter = cycle_length

    #     new_pos = (rotate_pos + k) % n
    #     mem, nums[new_pos] = nums[new_pos], mem
    #     rotate_pos = new_pos
    #     cycle_counter -= 1
    #     print(nums)

    # solution 1
    # copy the array, and find the new position
    n = len(nums)

    # copy vector
    out = [x for x in nums]
    for i in range(n):

        new_pos = (i + k) % n
        nums[new_pos] = out[i]

    print(nums)
    

if __name__ == '__main__':
    # rotate(nums = [1,2,3,4,5,6,7], k = 3)
    # rotate(nums = [-1,-100,3,99], k = 2)
    # rotate(nums = [1,2,3,4,5,6], k = 3)
    rotate(nums = [1,2,3,4,5,6], k = 4)