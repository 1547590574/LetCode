
class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        只需要判断当前整个字符串是不是回文串，因此只要碰到一个不符合条件的就返回False，这样可以快点结束循环
        """
        if x<0:
            return False
        else:
            count = 0
            xstr = str(x)
            while count < len(xstr) / 2:
                if xstr[count] != xstr[len(xstr) - 1-count]:       #不减一越界，数组最后一位是n-1
                    return False
                count+=1
            return True



S=Solution()
print(S.isPalindrome(121))