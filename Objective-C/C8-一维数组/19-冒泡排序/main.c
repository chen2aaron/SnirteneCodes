//
//  main.c
//  19-冒泡排序
//
//  Created by chan on 15/5/28.
//  Copyright (c) 2015年 chan. All rights reserved.
//

#include <stdio.h>
// 输入一组无序数据，使用冒泡排序进行输出
void fizz(int arr[], int len){
    for (int i=0; i<len-1; i++) {
        for (int j=0; j<len-1-i; j++) {
            if (arr[j] > arr[j+1]) {
                // 异或法交换值
                arr[j] = arr[j]^arr[j+1];
                arr[j+1] = arr[j]^arr[j+1];
                arr[j] = arr[j]^arr[j+1];
            }
        }
    }
}
int main(int argc, const char * argv[]) {
    int a[10]={2,54,23,6,53,1,423,9,44,39};
    fizz(a, 10);
    for (int i=0; i<10; i++) {
        printf("%d ",a[i]);
    }

    return 0;
}
