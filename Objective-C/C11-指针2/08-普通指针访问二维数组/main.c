//
//  main.c
//  08-普通指针访问二维数组
//
//  Created by chan on 15/5/31.
//  Copyright (c) 2015年 chan. All rights reserved.
//

#include <stdio.h>

int main(int argc, const char * argv[]) {
    int a[3][4]={1,3,5,7,9,11,13,15,17,19,21,23};
    int *p = a;
    for (int i=0; i<12; i++) {
        printf("%d  ", *(p+i));
    }
    return 0;
}
