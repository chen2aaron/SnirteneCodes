//
//  main.c
//  02-字符串结束符问题
//
//  Created by chan on 15/5/29.
//  Copyright (c) 2015年 chan. All rights reserved.
//

#include <stdio.h>

int main(int argc, const char * argv[]) {
    char ch1[] = {'a','b','\0'};
    char ch2[] = {'x','y','z'};
    // 先定义的高地址 从低到高 遇到\0停下 所以是xyzab
    printf("%s", ch2);
    return 0;
}
