class Solution:

    def merge_arrays(self,l1: list,l2: list):
        temp = l1.copy()
        for i in l2:
            temp.append(i)
        return temp

    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        merged_array = sorted(self.merge_arrays(nums1,nums2))
        if (len(merged_array) % 2):
            answer = merged_array[len(merged_array)//2]
        else:
            answer = (merged_array[len(merged_array)//2] + merged_array[(len(merged_array)//2)-1])/2
        return answer

obj = Solution()
print(obj.findMedianSortedArrays([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22],[0,6]))
