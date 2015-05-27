//
//  main.c
//  19-查看变量在内存中的每个字节
//
//  Created by chan on 15/5/27.
//  Copyright (c) 2015年 chan. All rights reserved.
//

#include <stdio.h>

int main(int argc, const char * argv[]) {
    int num = 10;
    printf("num = %d\n",num);
     for (int i=0; i<4; i++) {
        char *p = &num;
        printf("第%d个字节的地址:%p 值:%d\n",i+1, p+i, *(p+i));
    }



    return 0;
}
