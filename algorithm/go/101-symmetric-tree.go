/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
 思路： 递归的思想，其实就是看左右子树是否镜像对称，p q从根节点出发，当p指向左子节点时，q指向右子节点，
 当p指向右子节点时，q指向左子节点，一直到叶子节点
func isSymmetric(root *TreeNode) bool {
    return check(root, root)
}

func check(p,q *TreeNode) bool {
    if p == nil && q == nil {
        return true
    }
    if p == nil || q == nil {
        return false
    } 
    return p.Val == q.Val && check(p.Left, q.Right) && check(p.Right, q.Left)
}