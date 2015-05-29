//
//  main.c
//  14-用函数实现两个变量值交换
//
//  Created by chan on 15/5/30.
//  Copyright (c) 2015年 chan. All rights reserved.
//

#include <stdio.h>
/**
 *  内存释放了 交换不了
 *  实际是形参交换 跟实参无关
 */
void swap1(int a, int b){
    
    int temp;
    temp = a;
    a = b;
    b = temp;
}
/**
 *  内存释放了 交换不了
 *  实际是形参变量的地址交换
 */
void swap2(int *p1, int *p2){
    int *temp;
    temp = p1;
    p1 = p2;
    p2 = temp;
}
/**
 *  嘻嘻 交换成功
 */
void swap3(int *p1, int *p2){
    int temp;
    temp = *p1;
    *p1 = *p2;
    *p2 = temp;
    
}
int main(int argc, const char * argv[]) {
    int a = 4;
    int b = 5;
    printf("交换前：a = %d, b = %d\n",a, b);
//    swap1(a, b);
//    swap2(&a, &b);
    swap3(&a, &b);
    printf("交换后：a = %d, b = %d\n",a, b);
    return 0;
}
