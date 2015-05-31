//
//  main.c
//  05-指针数组
//
//  Created by chan on 15/5/31.
//  Copyright (c) 2015年 chan. All rights reserved.
//

#include <stdio.h>

int main(int argc, const char * argv[]) {
    int a = 1;
    int b = 2;
    int c = 3;
    int *p[3] = {&a,&b,&c};
//    打印指针数组的第一个元素的值
    printf("&a   = %p\n", &a);
    printf("p[0] = %p\n", p[0]);
//    打印指针数组的首地址
    printf("p    = %p\n", p);
    printf("&a[0]= %p\n", &p[0]);
//    访问a的值
    printf("&a   = %d\n", *&a);
    printf("p[0] = %d\n", *p[0]);
//    使用数组名来访问a的值
    printf("**p  = %d\n", **p);

    int arr[3][2] = {1,2,3,4,5,6};
    int *parr[3] = {arr[0],arr[1],arr[2]};
    printf("**parr = %d\n", **parr);
    printf("**(parr+1) = %d\n", **(parr+1));
    printf("**(parr+2) = %d\n", **(parr+2));
    return 0;
}
