//
//  main.c
//  13-从键盘接受数据构成 二维数组
//  从键盘上接受2个参数分别存放在m，n中
//  定义一个函数使用i*j初始化a[i][j]
//  定义一个函数打印二维数组的每个值
//  Created by chan on 15/5/29.
//  Copyright (c) 2015年 chan. All rights reserved.
//

#include <stdio.h>
/**
 这是一个二维数组的初始化函数
 */
void initArray(int m,int n,int arr[m][n]){
    for (int i=0; i<m; i++) {
        for (int j=0; j<n; j++) {
            arr[i][j] = (i+1)*(j+1);
        }
    }
}
/**
 *  遍历打印数组元素
 *
 *  @param m   行
 *  @param n   列
 *  @param arr 数组名
 */
void printArray(int m,int n,int arr[m][n]){
    for (int i=0; i<m; i++) {
        for (int j=0; j<n; j++) {
            printf("%d\t",arr[i][j]);
        }
        printf("\n");
    }
}

int main(int argc, const char * argv[]) {
    int m,n;
    printf("请输入数组行数和列数，用逗号分隔:\n");
    scanf("%d,%d",&m,&n);
    int arr[m][n];
    initArray(m, n, arr);
    printArray(m, n, arr);
    return 0;
}
