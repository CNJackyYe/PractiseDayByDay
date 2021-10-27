# 整数反转
# 给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。

# 如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。

# 假设环境不允许存储 64 位整数（有符号或无符号）。
#  

# 示例 1：

# 输入：x = 123
# 输出：321
# 示例 2：

# 输入：x = -123
# 输出：-321
# 示例 3：

# 输入：x = 120
# 输出：21
# 示例 4：

# 输入：x = 0
# 输出：0
#  

# 提示：

# -231 <= x <= 231 - 1

# 作者：力扣 (LeetCode)
# 链接：https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xnx13t/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

from typing import List


class Solution:
    def reverse(self, x: int) -> int:
        if x >= -2147483648 and x <= 2147483647:
            s = str(x)
            g = list(s)
            if g[0]=="-":
                g.pop(0)
                self.changeLocation(g)
                g=["-"]+g
                return int("".join(g))
            else:
                self.changeLocation(g)
                return int("".join(g))
        else:
            return 0

    def changeLocation(self, s:List[str])->List[str]:
        n = len(s)
        if n%2==0:
            for i in range(int(n/2)):
                t = s[i]
                s[i] = s[n-1-i]
                s[n-1-i] = t
        else:
            for i in range(int((n-1)/2)):
                t = s[i]
                s[i] = s[n-1-i]
                s[n-1-i] = t
        return s
            



su = Solution()
print(su.reverse(900000))