# Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

# Return the array in the form [x1,y1,x2,y2,...,xn,yn].

# nums = [2, 5, 1, 3, 4, 7]
# n = 3

# nums = [1,2,3,4,4,3,2,1]
# n = 4

# nums = [1,1,2,2]
#  n = 2


class Solution:
    # def shuffle(self, nums: List[int], n: int) -> List[int]:
    def shuffle(self, nums, n):
        temp = []
        for i in range(n):
            temp.append(nums[i])
            temp.append(nums[n + i])
        return temp
