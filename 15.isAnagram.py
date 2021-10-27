# 有效的字母异位词
# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

# 示例 1:

# 输入: s = "anagram", t = "nagaram"
# 输出: true
# 示例 2:

# 输入: s = "rat", t = "car"
# 输出: false
# 说明:
# 你可以假设字符串只包含小写字母。

# 进阶:
# 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？

# 相关标签
# 排序
# 哈希表

# 作者：力扣 (LeetCode)
# 链接：https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xn96us/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) == len(s):
            tdic = {}
            sdic = {}
            for i in t:
                if tdic.get(i) == None:
                    tdic[i] = 1
                else:
                    tdic[i] +=1
            for i in s:
                if sdic.get(i) == None:
                    sdic[i] = 1
                else:
                    sdic[i] +=1
            for j in tdic.keys():
                if tdic.get(j) != sdic.get(j):
                    return False
            return True
        return False


su = Solution()
print(su.isAnagram("rat", "car"))
