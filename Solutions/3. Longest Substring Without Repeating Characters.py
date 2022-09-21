class Solution:

    def check_repeating(self,sub):
        for letter in sub:
            if sub.count(letter) > 1:
                return False
        return True

    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = 0
        left = 0
        right = 1
        while left != right:
            sub = ""
            for i in range(left,right):
                if i < len(s):
                    sub = sub+s[i]
            if self.check_repeating(sub):
                if len(sub) > answer:
                    answer = len(sub)
                #
                if len(s) > right:
                    right = right + 1
                else:
                    left = left + 1

            else:
                left = left + 1
        return answer


obj = Solution()
print(obj.lengthOfLongestSubstring(" "))