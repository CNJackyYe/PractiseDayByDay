# 验证回文串
# 给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

# 说明：本题中，我们将空字符串定义为有效的回文串。

# 示例 1:

# 输入: "A man, a plan, a canal: Panama"
# 输出: true
# 示例 2:

# 输入: "race a car"
# 输出: false
# 相关标签
# 双指针
# 字符串

# 作者：力扣 (LeetCode)
# 链接：https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xne8id/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=re.sub(r"[^A-Za-z0-9]","",s).lower()
        for i in range(len(s)):
            if(s[i]!=s[-1-i]):
                return False
        print(s)
        return True


su = Solution()
print(su.isPalindrome("A man, a plan, a canal: Panama"))