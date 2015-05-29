//
//  main.c
//  05-字符串处理函数
//
//  Created by chan on 15/5/29.
//  Copyright (c) 2015年 chan. All rights reserved.
//

#include <stdio.h>
#include <string.h>

int main(int argc, const char * argv[]) {

    char str[]="python";
    puts(str);  // 不能格式化输出
    puts(&str[2]);
//    char str1[100];
//    gets(str1); // 存在越界问题
//    puts(str1);
    char ch2[100]="life is short ";
    char ch3[]="I use python";
    strcat(ch2, ch3);
    puts(ch2);
    
    strcpy(ch2, ch3);
    puts(ch2);
    
    char str1[]="haha";
    char str2[]="xixi";
    int s = strcmp(str1, str2);
    printf("%d\n", s);
    
    int len = strlen(str1);
    printf("%d\n", len);
    return 0;
}
