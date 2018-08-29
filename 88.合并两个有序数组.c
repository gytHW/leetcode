//思路：由于合并后A数组的大小必定是m+n，所以从最后面开始往前赋值，先比较A和B中最后一个元素的大小，把较大的那个插入到m+n-1的位置上，再依次向前推。如果A中所有的元素都比B小，那么前m个还是A原来的内容，没有改变。如果A中的数组比B大的，当A循环完了，B中还有元素没加入A，直接用个循环把B中所有的元素覆盖到A剩下的位置。
void merge(int* nums1, int m, int* nums2, int n) {
    int i = m-1;
    int j = n-1;
    int k = m+n-1;

    while(i>=0 && j>=0)
    {
        if(nums1[i] < nums2[j])
        {
            nums1[k] = nums2[j];
            j--;
        } else {
            nums1[k] = nums1[i];
            i--;
        }
        k--;
    }
    
    //如果nums2有剩余元素
    while(j>=0)
    {
        nums1[k] = nums2[j];
        j--;
        k--;
    }
    
    //因为是合并到nums1数组中，所以如果是nums1有剩余元素，剩余元素本来就是nums1的开始值那直接保持原值就行，不必再替换
    // while(i>=0)
    // {
    //     nums1[k] = nums1[i];
    //     i--;
    //     k--;
    // }
}