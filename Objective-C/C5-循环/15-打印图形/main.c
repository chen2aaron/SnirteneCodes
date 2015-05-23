//
//  main.c
//  15-打印图形
//
//  Created by chan on 15/5/24.
//  Copyright (c) 2015年 chan. All rights reserved.
//

#include <stdio.h>

int main(int argc, const char * argv[]) {
//    长方形
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
            printf("* ");
        }
        printf("\n");
    }
//    三角形
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j <= i; j++) {
            printf("* ");
        }
        printf("\n");
    }
//    倒三角
    for (int i = 0; i < 5; i++) {
        for (int j = 5; j > i; j--) {
            printf("* ");
        }
        printf("\n");
    }
//    等边三角
    for (int i = 0; i < 5; i++) {
        for (int j = 5; j > i; j--) {
            printf(" ");
        }

        for (int j = 0; j <= i; j++) {
            printf("* ");
        }
        printf("\n");
    }
    return 0;
}
