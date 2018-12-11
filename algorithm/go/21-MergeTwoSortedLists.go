/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func mergeTwoLists(l1 *ListNode, l2 *ListNode) *ListNode {
    if l1 == nil {
        return l2
    }
    if l2 == nil {
        return l1
    }
    var list *ListNode
    if l1.Val >= l2.Val {
        list = l2
        list.Next = mergeTwoLists(l1, l2.Next)
    }
    if l1.Val < l2.Val {
        list = l1
        list.Next = mergeTwoLists(l1.Next, l2)
    }
    return list
}