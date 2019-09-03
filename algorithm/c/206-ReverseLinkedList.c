/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

/*迭代*/
/*思路：参见《看图理解单链表反转》https://www.cnblogs.com/mafeng/p/7149980.html*/
struct ListNode* reverseList(struct ListNode* head){
    if (head == NULL || head->next == NULL)
        return head;
    struct ListNode *p = head;
    struct ListNode *q = p->next;
    head->next = NULL;
    while(q)
    {
        struct listNode *tmp = q->next;
        q->next = p;
        p = q;
        q = tmp;
    }
    return p;
}

/*递归*/
/**思路：递归的思路很简单，假如有个A->B->C->D->E,假设BCDE已经反转好,即A->B<-C<-D<-E，此时只需要把A反转，即把BCDE这一块指向A，
 * 即A->next->next = A,BCDE内部递归执行即可
 **/
struct ListNode* reverseList_1(struct ListNode* head){
    if (head == NULL || head->next == NULL)
        return head;
    struct ListNode* newHead = reverseList(head->next);
    head->next->next = head;
    head->next = NULL;
    return newHead;
}