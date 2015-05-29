//
//  main.c
//  01-字符串输入输出
//
//  Created by chan on 15/5/29.
//  Copyright (c) 2015年 chan. All rights reserved.
//

#include <stdio.h>

int main(int argc, const char * argv[]) {
    char str[]="python";
    for (int i=0; i<sizeof(str); i++) {
        printf("%c", str[i]);
    }
    // 从给定的地址开始 一直输出字符 一直到\0结束
    printf("\n%s\n", str);
    printf("%s\n", &str[0]);
    printf("%s\n", &str[3]);
    return 0;
}
