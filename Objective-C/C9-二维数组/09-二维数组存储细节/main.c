//
//  main.c
//  09-二维数组存储细节
//
//  Created by chan on 15/5/29.
//  Copyright (c) 2015年 chan. All rights reserved.
//

#include <stdio.h>

int main(int argc, const char * argv[]) {
    int a[2][4]={2,4,7,8,33,22,9,444};
    //二维数组首地址＝数组名＝&a[0]=&a[0][0]
    printf("a        = %p\n",a);
    printf("&a[0]    = %p\n",a[0]);
    printf("&a[0][0] = %p\n",&a[0][0]);
    //二维数组第二行地址
    printf("&a[1]    = %p\n",a[1]);
    printf("&a[1][0] = %p\n",&a[1][0]);
    printf("-----------------------------\n");
    
    //遍历地址
    for (int i=0; i<2; i++) {
        for (int j=0; j<4; j++) {
            printf("&a[%d][%d] = %p\n",i,j,&a[i][j]);
        }
    }
    //总字节数 = 元素个数*类型
    int len1 = 2*4*sizeof(int);
    int len2 = sizeof(a);
    printf("len1 = %d\n",len1);
    printf("len2 = %d\n",len2);
    //每行占用字节数
    int len_bite = sizeof(a[0]);
    printf("每行字节数 = %d\n",len_bite);
    //有多少行 = 总字节数 / 每行占用字节数
    int len_row = sizeof(a)/sizeof(a[0]);
    printf("len_row = %d\n",len_row);
    //有多少列 = 每行占用字节数 / 每个元素类型
    int len_col = sizeof(a[0])/sizeof(int);
    printf("len_col = %d\n",len_col);
    return 0;
}
