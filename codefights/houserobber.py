# https://codefights.com/interview/GFhev49JRkvy9tA5e/description
# python3

from functools import lru_cache

def houseRobber(nums):
    return house(tuple(nums))

@lru_cache(maxsize=1000)
def house(nums):
    if len(nums) == 0:
        return 0
    return max(house(nums[1:]), house(nums[2:]) + nums[0])
