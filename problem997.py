from typing import List


class Solution:
    # 用空换时间，两个列表 一个记录被多少人信任，一个纪录谁信任其他人（类似于倒排索引的思想）
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        be_trusted = [0] * n
        trust_to = []
        for i, j in trust:
            trust_to.append(i)
            be_trusted[j - 1] += 1
        print(be_trusted)
        for i in range(len(be_trusted)):
            if be_trusted[i] == n - 1:
                if i + 1 not in trust_to:
                    return i + 1
                else:
                    return -1
        return -1


s = Solution()
print(s.findJudge(3, [[1, 3], [2, 3], [3, 1]]))
