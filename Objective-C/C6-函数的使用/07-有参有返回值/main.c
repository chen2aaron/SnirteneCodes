//
//  main.c
//  07-有参有返回值
//
//  Created by chan on 15/5/24.
//  Copyright (c) 2015年 chan. All rights reserved.
//

#include <stdio.h>

int max(int x,int y){
    // 跟python的这句好像啊！！！！第二次学习C语言好轻松～
    // return x if x > y else y
    return x>y?x:y;
}
int main(int argc, const char * argv[]) {
    int m = max(8,5);
    printf("max = %d\n", m);
    return 0;
}
