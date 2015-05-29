//
//  main.c
//  15-指针常见的应用场景
//
//  Created by chan on 15/5/30.
//  Copyright (c) 2015年 chan. All rights reserved.
//

#include <stdio.h>

//1.在被调函数中可以修改主调函数中变量的值
void changeValue(int *p){
    *p = 100;
}

//2.让函数可以有多个返回值
void calculator(int x, int y, int *plus, int *minus, int *mul, float *div){
    *plus = x + y;
    *minus = x - y;
    *mul = x * y;
    *div = (float)x / y;
}
int main(int argc, const char * argv[]) {
    int a = 1;
    int *p1 = &a;
    printf("%p\n", p1);
    printf("%p\n", &a);
    printf("%d\n", *p1);
    printf("%d\n", a);
    changeValue(p1);
    printf("%d\n", a);
    int plus = 0;
    int minus = 0;
    int mul = 0;
    float div = 0.0;
    calculator(4, 6, &plus, &minus, &mul, &div);
    printf("加减乘除结果分别是：%d %d %d %.2f\n",plus, minus, mul, div);
    return 0;
}
