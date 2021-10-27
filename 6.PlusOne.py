# 加一 2021-02-01
# 给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。
# 最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
#
# 解释：如整数99会表示为[9,9]这种形式，现在要写一个程序让99加1,即输出[1,0,0]
# 只允许进行数组内操作
#
# 示例1：
#
# 输入：digits = [9,9]
# 输出：[1,0,0]
# 解释：输入数组表示数字 99。
# 示例2：
#
# 输入：digits = [4,3,2,1]
# 输出：[4,3,2,2]
# 解释：输入数组表示数字 4321。
# 示例 3：
#
# 输入：digits = [0]
# 输出：[1]
#
#
# 提示：
#
# 1 <= digits.length <= 100
# 0 <= digits[i] <= 9
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        pass


# 结果测试 https://leetcode-cn.com/problems/plus-one/