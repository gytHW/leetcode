#include <stdio.h>
#include <stdlib.h>

int climbStairs(int n) {
    int *num = (int *)calloc(n, sizeof(int));
    if (n == 1) {
        return 1;
    }
    if (n == 2) {
        return 2;
    }
    //直接递归写法会爆栈超时
    // num = climbStairs(n-1) + climbStairs(n-2);
    //return num;
    num[0] = 1;
    num[1] = 2;
    for (int i=2;i<n;i++) {
        num[i] = num[i-1] + num[i-2];
    }
    return num[n-1];
}