//
//  main.c
//  14-找最大值
//
//  Created by chan on 15/5/28.
//  Copyright (c) 2015年 chan. All rights reserved.
//

#include <stdio.h>

int main(int argc, const char * argv[]) {
    int num[10]={0};
    printf("请输入10个数\n");
    for (int i=0; i<10; i++) {
        printf("请输入第%d个数\n",i+1);
        scanf("%d",&num[i]);
    }
    int max=0;
    for (int i=0; i<10; i++) {
        if (num[i]>max) {
            max=num[i];
        }
    }
    printf("max = %d\n",max);
    return 0;
}
