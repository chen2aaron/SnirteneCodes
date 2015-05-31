//
//  main.c
//  09-二维数组指针定义和初始化
//
//  Created by chan on 15/5/31.
//  Copyright (c) 2015年 chan. All rights reserved.
//

#include <stdio.h>

int main(int argc, const char * argv[]) {
    int a[3][4]={1,3,5,7,9,11,13,15,17,19,21,23};
    int (*p)[4] = a;

    for (int i=0; i<3; i++) {
        for (int j=0; j<4; j++) {
            printf("%d\t", *(*(p+i)+j));
        }
        printf("\n");
    }
    printf("----------------------\n");
    for (int j=0; j<3; j++) {
        printf("%d\t", *(*(p++)+j));
    }
    return 0;
}
