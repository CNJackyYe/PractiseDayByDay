# 字符串中的第一个唯一字符
# 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

#  

# 示例：

# s = "leetcode"
# 返回 0

# s = "loveleetcode"
# 返回 2
#  

# 提示：你可以假定该字符串只包含小写字母。

# 相关标签
# 哈希表
# 字符串

# 作者：力扣 (LeetCode)
# 链接：https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xn5z8r/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution:
    def firstUniqChar(self, s: str) -> int:
        res = {}
        n = len(s)
        for i in range(n):
            if(res.get(s[i])==None):
                res[s[i]] = i
            else:
                res[s[i]] = "a"
        if res!={}:
            print(res)
            for i in res.items():
                if i[1] != "a":
                    return i[1]
            return -1
        else:
            return -1

su = Solution()

print(su.firstUniqChar("leetcode"))
print(su.firstUniqChar("loveleetcode"))
print(su.firstUniqChar("aadadaad"))