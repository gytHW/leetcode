// 面试遇到，要求时间复杂度为O(n)的话，简单遍历是不行的。因为hashmap的查找是O(1)，所以这里考虑用map，
// 一个map保存值到下标的映射，以值为key，可以迅速通过一个值查到是否在map中存在。然后对于数组中每一个值，
// 只需要知道目标target和这个值的差是否在map中即可，如果不存在就把值保存到map。
func twoSum(nums []int, target int) []int {
    m := map[int]int{}

    for k,v := range nums {
        diff := target - v
        if index, ok := m[diff];ok {
            return []int{index, k}
        }
        m[v] = k 
    }
    return nil
}