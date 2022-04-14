class Solution:
    # 二分法查找在开平方根上的应用，
    # def mySqrt(self, x: int) -> int:
    #         if x == 1:
    #             return 1
    #         minV, maxV = 0, x
    #         while maxV - minV > 1:
    #             mid = (minV + maxV) // 2
    #             if x / mid < mid:
    #                 maxV = mid
    #             else:
    #                 minV = mid
    #         return int(minV)


    # 尝试刚学的Newton迭代法,当作根 不知道 尝试用a去做根的初始迭代值，会慢慢向真正的根 根号a收敛，由于交给计算机运算，收敛快慢无所谓
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return int(x)
        r = x/2
        a= x/r # 真如评论区所说，存一下会更快
        while a < r:
            a=x/r
            r = (r + a) // 2
        return int(r)

s = Solution()
print(s.mySqrt(5))
