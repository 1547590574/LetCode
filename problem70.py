import functools


class Solution:
    # 只有当function的所有参数可以hash（数据不可变类型，int，float，bool等）时才能使用装饰器，此装饰器的作用是在内存中开辟一道缓存区，当遇到参数相同的方法时直接得出返回值，不用重复计算。
    @functools.lru_cache(100)
    def climbStairs(self, n: int) -> int:
        if n <=2:
            return n
        else:
            return self.climbStairs(n-2) + self.climbStairs(n - 1)

s=Solution()
print(s.climbStairs(44))