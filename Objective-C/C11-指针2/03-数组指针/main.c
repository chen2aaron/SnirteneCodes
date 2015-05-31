//
//  main.c
//  03-数组指针
//
//  Created by chan on 15/5/31.
//  Copyright (c) 2015年 chan. All rights reserved.
//

#include <stdio.h>

int main(int argc, const char * argv[]) {
    int a[]={2,4,6,7,8,10};
    int *p = a;
    for (int i=0; i<6; i++) {
        printf("%d\t", *p++);
    }
    return 0;
}
