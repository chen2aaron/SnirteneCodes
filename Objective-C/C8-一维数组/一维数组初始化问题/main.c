//
//  main.c
//  一维数组初始化问题
//
//  Created by chan on 15/5/28.
//  Copyright (c) 2015年 chan. All rights reserved.
//

#include <stdio.h>

int main(int argc, const char * argv[]) {
    int a[10]={[5]=2333};
    float f1[10]={2.3};
    char ch[10]={'a','b','c'};
    for (int i=0; i<10; i++) {
//        printf("%d\t",a[i]);
//        printf("%.2f\t",f1[i]).cb```;
        printf("%d\t",ch[i]);
    }
    return 0;
}
