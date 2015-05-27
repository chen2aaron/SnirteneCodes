//
//  main.c
//  17-变量值交换
//
//  Created by chan on 15/5/27.
//  Copyright (c) 2015年 chan. All rights reserved.
//

#include <stdio.h>
/**
 1.临时变量
    temp=a
    a=b
    b=temp
 -------------
 2.不需要变量
    a=a+b
    b=a-b
    a=a-b
 -------------
 3.按位 异或方式
    a=a^b
    b=a^b
    a=a^b
 */
int main(int argc, const char * argv[]) {
    int a = 3;
    int b = 4;
    printf("a = %d, b = %d\n", a, b);
    a=a^b;
    b=a^b;
    a=a^b;
    printf("a = %d, b = %d\n", a, b);
    return 0;
}
