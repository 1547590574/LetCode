# <---coding: utf-8--->
# @Time:  2022/5/4/18:03
# @Author = posiondy
# @Email: 1547590574@qq.com
# @Software: PyCharm
import collections
# 这是队列模拟的方法，一定要记住，每次被淘汰的人自动进入队列尾部，这里的deque是一个双向队列，可以poeleft也可以popright
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        q = collections.deque(range(1, n + 1))
        while len(q) > 1:
            for i in range(k-1):
                q.append(q.popleft())
            q.popleft()
        return q[0]

# 接下来考虑一下纯数学的方法,公式是倒着推的，因为返回的是编号，而我用的是数组中下标，所以+1
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        p = 0
        for i in range(2, n+1):
            p = (p + k) % i

        return p + 1