from typing import List

class Solution:    
    def insertion_sort(self, arr: List[int]) -> List[int]:
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1

            while j >= 0 and arr[j] < key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

        return arr
    
sol = Solution()
nums = [52, 7, 22, 61, 90, 35]
print(sol.insertion_sort(nums))