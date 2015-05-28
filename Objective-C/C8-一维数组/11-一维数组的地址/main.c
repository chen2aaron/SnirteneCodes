//
//  main.c
//  11-一维数组的地址
//
//  Created by chan on 15/5/28.
//  Copyright (c) 2015年 chan. All rights reserved.
//

#include <stdio.h>

int main(int argc, const char * argv[]) {
    int x[]={1, 2};
    char ca[5]={'a','B','C','D','E'};
    //先定义的数组分配在高地址
    printf("x = %p\n",x); //高地址
    printf("ca= %p\n",ca);//低地址
    //ca[0]低地址
    //ca[4]高地址
    printf("ca = %p\n",ca);//数组名是个常量，代表了数组的首地址
    for (int i=0; i<5; i++) {
        printf("ca[%d] = %p\n",i,&ca[i]);
    }
    return 0;
}
