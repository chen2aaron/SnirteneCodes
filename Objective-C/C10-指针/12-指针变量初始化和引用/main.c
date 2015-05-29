//
//  main.c
//  12-指针变量初始化和引用
//
//  Created by chan on 15/5/30.
//  Copyright (c) 2015年 chan. All rights reserved.
//

#include <stdio.h>

int main(int argc, const char * argv[]) {
    // *的用法：1）定义指针变量
    //         2) 存储指针变量指向的存储空间的内容
    int a = 4;
    int *p = &a;
    *p = 100; // 设定值 间接传值
    int value = *p; // 获取指针变量指向的内存空间的内容
    printf("*p = %p, value = %d, a = %d\n",p, value, a);
    return 0;
}
