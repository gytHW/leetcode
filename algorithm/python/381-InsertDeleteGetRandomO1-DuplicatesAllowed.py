#思路： 参照380题，但是testcese一直不能通过，最后参考别人把getRandom中获取随机数的方式从random.randint换成random.randrange就AC了
#       原因不明，以后再看看 现在夜里2点了
import random

class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.RandomList = []
        

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        exist = True
        if val in self.RandomList:
            exist = False
        self.RandomList.append(val)
        return exist
        

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.RandomList:
            key = self.RandomList.index(val)
            self.RandomList.pop(key)
            return True
        return False
        

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        if not self.RandomList:
            return None
        randomNum = random.randrange(0, len(self.RandomList))
        return self.RandomList[randomNum-1]
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()https://leetcode-cn.com/submissions/detail/6675144/