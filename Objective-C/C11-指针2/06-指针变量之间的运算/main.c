//
//  main.c
//  06-指针变量之间的运算
//
//  Created by chan on 15/5/31.
//  Copyright (c) 2015年 chan. All rights reserved.
//

#include <stdio.h>
//减法运算：
//    判断2个指针变量指向的元素是否连续
//    判断2个指针变量之间相隔几个元素
int main(int argc, const char * argv[]) {
    int arr[5]={1,2,3,4,5};
    int *p1 = arr;
    int *p2 = &arr[3];
//    判断2个指针变量之间相隔几个元素
    printf("p2-p1 = %ld\n", p2-p1); //相隔3个元素
    printf("p1-p2 = %ld\n", p1-p2);
    
    
//    判断2个指针变量指向的元素是否连续
    printf("p2>p1 = %d\n", p2>p1); // 1:p2高位 0:p2低位或同位

    return 0;
}
