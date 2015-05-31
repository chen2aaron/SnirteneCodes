//
//  main.c
//  07-用数组名访问二维数组
//
//  Created by chan on 15/5/31.
//  Copyright (c) 2015年 chan. All rights reserved.
//

#include <stdio.h>

int main(int argc, const char * argv[]) {
    int a[3][4]={1,3,5,7,9,11,13,15,17,19,21,23};
    // 列指针 地址
    printf("&a[0][0] = %p\n", &a[0][0]);
    printf(" a[0]    = %p\n", a[0]);
    printf("&a[0][1] = %p\n", &a[0][1]);
    printf(" a[0]+1  = %p\n", a[0]+1);
    printf("&a[0][2] = %p\n", &a[0][2]);
    printf(" a[0]+2  = %p\n", a[0]+2);
    printf("-----------------------\n");
    
    // 行指针 地址
    printf("a        = %p\n", a);
    printf("a[0]     = %p\n", a[0]);
    printf("a+1      = %p\n", a+1);
    printf("a[1]     = %p\n", a[1]);
    printf("a+2      = %p\n", a+2);
    printf("a[2]     = %p\n", a[2]);
    printf("-----------------------\n");
    
    printf("a+1      = %p\n", a+1);
    printf("a[1]     = %p\n", a[1]);
    printf("*(a+1)   = %p\n", *(a+1));
    printf("&a[1][0] = %p\n", &a[1][0]);
    
    // 第i行j列的值
    // *(a[i]+j) = a[i][j]
    // a[i] = *(a+i)
    // *(*(a+i)+j) = a[i][j]
    printf("a[1][2]     = %d\n", a[1][2]);
    printf("*(a[1]+2)   = %d\n", *(a[1]+2));
    printf("*(*(a+1)+2) = %d\n", *(*(a+1)+2));
    return 0;
}
