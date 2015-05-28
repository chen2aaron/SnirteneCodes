//
//  main.c
//  08-遍历二维数组
//
//  Created by chan on 15/5/29.
//  Copyright (c) 2015年 chan. All rights reserved.
//

#include <stdio.h>

int main(int argc, const char * argv[]) {
    int a[3][4]={1,2,5,7,8,4,12,57,56,22,44,89};
    printf("%d\n",a[2][2]);
    for (int i=0; i<3; i++) {
        for (int j=0; j<4; j++) {
            printf("a[%d][%d]=%d\t",i,j,a[i][j]);
        }
        printf("\n");
    }
    return 0;
}
