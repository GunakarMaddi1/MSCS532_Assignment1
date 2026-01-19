from typing import List

class Solution:    
    def insertion_sort(self, arr: List[int]) -> List[int]:
        """
        Sort the input array in monotonically decreasing order 
        using Insertion Sort Algorithm
        """

        # Traverse from the second element to the end of the array
        for i in range(1, len(arr)):
            key = arr[i] # store the current element as key
            j = i - 1 # j points to the last index of the sorted part

            while j >= 0 and arr[j] < key: # shift elements by one position to the right if they are smaller
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key #insert key at correct position

        return arr
    
sol = Solution()
nums = [52, 7, 22, 61, 90, 35]
print(sol.insertion_sort(nums))