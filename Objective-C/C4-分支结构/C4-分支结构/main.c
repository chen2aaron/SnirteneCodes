//
//  main.c
//  C4-分支结构
//
//  Created by chan on 15/5/23.
//  Copyright (c) 2015年 chan. All rights reserved.
//

#include <stdio.h>
/**
 *  判断输入的数是否是5
 *
 *  必须是双引号
 *
 *
 */
int main(int argc, const char * argv[]) {
    int num = 0;
    printf("请输入一个数：");
    
    scanf("%d",&num);
    if (num != 5) {
        printf("很遗憾 错了");
    }
    else printf("恭喜对了\n");
    return 0;
}
