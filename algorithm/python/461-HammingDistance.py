#思路：两个整数之间的汉明距离指的是这两个数字对应二进制位不同的位置的数目。所以很容易可以想到异或，异或之后二进制数1的个数就是不同位置数目
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x^y).count('1')