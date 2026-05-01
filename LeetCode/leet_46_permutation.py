from typing import List
import itertools
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        print(list(itertools.permutations(nums)))
        print(list(itertools.combinations(range(1,5),2)))

nums= [1,2,3]
c = Solution()
c.permute(nums)


