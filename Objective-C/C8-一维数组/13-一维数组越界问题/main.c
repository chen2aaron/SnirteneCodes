//
//  main.c
//  13-一维数组越界问题
//
//  Created by chan on 15/5/28.
//  Copyright (c) 2015年 chan. All rights reserved.
//

#include <stdio.h>

int main(int argc, const char * argv[]) {
    char a[2]={'p','y'};
    printf("a[0] = %c\n", a[0]);
    printf("a[1] = %c\n", a[1]);
    // 数组越界危害极大
    a[2]='t';
    printf("a[2] = %d\n", a[2]);
    return 0;
}
