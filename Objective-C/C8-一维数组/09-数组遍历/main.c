//
//  main.c
//  09-数组遍历
//
//  Created by chan on 15/5/28.
//  Copyright (c) 2015年 chan. All rights reserved.
//

#include <stdio.h>
//从键盘输入一个数组长度,构建一个数组,然后在通过for循环从键盘接受数字给
//数组初始化.并使用for循环输出查看
int main(int argc, const char * argv[]) {
    int len;
    printf("请输入数组的长度：\n");
    scanf("%d",&len);
    int a[len];
    for (int i=0; i<len; i++) {
        printf("请数组的%d个值\n",i+1);
        scanf("%d",&a[i]);
    }
    for (int i=0; i<len; i++) {
        printf("%d\t",a[i]);
    }
    return 0;
}
