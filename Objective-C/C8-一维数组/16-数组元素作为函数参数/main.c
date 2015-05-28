//
//  main.c
//  16-数组名作为函数参数
//
//  Created by chan on 15/5/28.
//  Copyright (c) 2015年 chan. All rights reserved.
//

#include <stdio.h>
void change(int arr[2]){
    printf("arr = %p\n",arr);
    arr[0]=18;
}
int main(int argc, const char * argv[]) {
    int a[2]={1, 2};
    // 实参是数组名a，形参是arr
    // 此时 a和arr在内存中代表了同一块内存空间
    // 用数组名作为函数参数，传递的是地址
    change(a);
    printf("a = %p\n", a);
    printf("a[0] = %d\n", a[0]);
    return 0;
}
