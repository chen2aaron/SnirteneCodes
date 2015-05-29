//
//  main.c
//  08-单词首字母大写并统计单词个数
//
//  Created by chan on 15/5/29.
//  Copyright (c) 2015年 chan. All rights reserved.
//

#include <stdio.h>

int main(int argc, const char * argv[]) {
    char str[100];
    int words = 0;
    int count = 0;
    printf("请输入一个字符串：\n");
    gets(str);
    for (int i=0; str[i]!='\0'; i++) {
        if (str[i]==' ') {
            words = 0; //标记是单词
        }
        else if (words == 0) {
            count++;
            str[i] -= 32;
            words = 1; // 标记不是单词
        }
    }
    printf("单词个数：%d，字符串：%s\n", count, str);
    return 0;
}
