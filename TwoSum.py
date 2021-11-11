class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_num = {}
        index = 0
        for element in nums:           
            if target-element in hash_num:
                val = hash_num[target-element]
                return [val, index]
            else:
                hash_num[element] = index
            index+=1
