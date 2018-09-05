/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
bool hasCycle(struct ListNode *head) {
    ListNode *p;
    ListNode *q;
    if(head == NULL) {
    	return false;
    }
    p = head;
    q = head->next;

    if(p!=NULL && q!=NULL && q->next!=NULL && p!=q) {
    	p = p->next;
    	q = q->next->next;
    }
    if( p == q) 
    	return true;
    else
    	return false;
}