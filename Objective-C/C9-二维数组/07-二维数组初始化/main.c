//
//  main.c
//  07-二维数组初始化
//
//  Created by chan on 15/5/29.
//  Copyright (c) 2015年 chan. All rights reserved.
//

#include <stdio.h>

int main(int argc, const char * argv[]) {
    //完全初始化
    int a[2][3]={{1,2,3},{4,5,6}};
    int b[2][3]={1,2,3,4,5,6};
    int c[][2]={1,2,3,4,5,6};//==int c[3][2]
    //部分初始化
    int d[3][4]={1};//只有d[0][0]=1 其他都是0
    int e[3][4]={{1},{2},{3}};//每行第一个数赋值
    int f[3][4]={1,2,3,4,5};//顺着赋值
    return 0;
}
