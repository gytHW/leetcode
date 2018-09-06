class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) < 3: #1个或2个元素必定是单调数组
            return True
        if max(A) == min(A): #特殊情况，所有元素值都一样的list
            return True
        order = 'asc' if A[0] < A[-1] else 'desc'
        for i in range(len(A)-1):
            if order == 'asc' and A[i] > A[i+1]:
                    return False
            if order == 'desc' and A[i] < A[i+1]:
                    return False
        return True