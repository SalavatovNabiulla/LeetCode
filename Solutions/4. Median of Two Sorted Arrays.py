class Solution:

    def merge_arrays(self,l1: list,l2: list):
        for i in l2:
            l1.append(i)
        return l1

    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        answer: float = 0
        merged_array = sorted(self.merge_arrays(nums1,nums2))
        if len(merged_array) > 2:
            summ = 0
            for i in range(1,len(merged_array)-1):
                summ = summ+merged_array[i]
            answer = summ/(len(merged_array)-2)
            if str(answer - int(answer))[2] != "5":
                answer = float(int(answer))
        elif len(merged_array) == 2:
            summ = 0
            for i in range(0,len(merged_array)):
                summ = summ+merged_array[i]
            answer = summ/len(merged_array)
        elif len(merged_array) == 1:
            return float(merged_array[0])
        elif len(merged_array) == 0:
            return float(0)

        return answer

obj = Solution()
print(obj.findMedianSortedArrays([],[-3,-2,-1,1,5]))
#Input: nums1 = [1,2], nums2 = [3,4]
#Output: 2.50000
#Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
