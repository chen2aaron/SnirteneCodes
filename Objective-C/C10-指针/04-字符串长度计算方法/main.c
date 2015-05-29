//
//  main.c
//  04-字符串长度计算方法
//
//  Created by chan on 15/5/29.
//  Copyright (c) 2015年 chan. All rights reserved.
//

#include <stdio.h>

int main(int argc, const char * argv[]) {
    // 字符串长度恰好等于数组在内存中占用的字符数
    char str[]="abc";
    printf("%ld\n",sizeof(str));
    char str1[]="abc\0def";
    printf("%ld\n",sizeof(str1));
    printf("%s\n",str1);
    

    return 0;
}
