#思路： 这是一道设计题，使用set集合数据结构可以满足要求，需注意，获取随机值的时候，因为set没有key可以用来取值，所以转成list，再利用随机key完成功能。

import random

class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.RandomSet = set([])

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.RandomSet:
            self.RandomSet.add(val)
            return True
        else:
            return False
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.RandomSet:
            self.RandomSet.remove(val)
            return True
        return False
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        if not self.RandomSet:
            return None
        RandomList = list(self.RandomSet)
        randomNum = random.randint(0, len(RandomList)-1) #randint取随机数是两边都包含的闭区间
        return RandomList[randomNum]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()