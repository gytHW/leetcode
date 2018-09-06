#思路：用一个Set保存所有数组中出现过的数字，然后遍历范围内所有数字，不存在于set中的就是未出现过的
class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        record = set(nums)
        n = len(nums)
        res = []
        #需注意，range(m, n)是不包含n这个数的，所以这里需要range(1, n+1)
        #另外,遍历的两个方式range和xrange，range是生成一个数组，而xrange是一个生成器，会比range节省空间
        #在python3中，xrange改名成range了，需要注意这一点，所以这里写range就可以了
        #btw,往list中添加元素用append，这点跟php等不同
        for i in range(1, n+1):
            if i not in record:
                res.append(i)
        return res