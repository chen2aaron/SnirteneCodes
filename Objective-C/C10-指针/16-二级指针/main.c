//
//  main.c
//  16-二级指针
//
//  Created by chan on 15/5/30.
//  Copyright (c) 2015年 chan. All rights reserved.
//

#include <stdio.h>

int main(int argc, const char * argv[]) {
    int a = 5;
    int *p = &a;
    printf("&a = %p\n", &a);
    printf("p  = %p\n", p);
    int **p1 = &p;
    printf("p  = %p\n", &p);
    printf("&p = %p\n", p1);
    printf("*p = %d\n", *p);
    printf("*p1= %p\n", *p1);
    printf("**p1= %d\n", **p1);
    return 0;
}
