//
//  main.c
//  02-选择排序代码实现
//
//  Created by chan on 15/5/29.
//  Copyright (c) 2015年 chan. All rights reserved.
//

#include <stdio.h>
/**
 *  选择排序
 */
void selectSort(int arr[], int len){
    for (int i=0; i<len-1; i++) {
        for (int j=i+1; j<len; j++) {
            if (arr[i]>arr[j]) {
                arr[i]=arr[i]^arr[j];
                arr[j]=arr[i]^arr[j];
                arr[i]=arr[i]^arr[j];
            }
        }
    }
}
int main(int argc, const char * argv[]) {
    //
    int a[10]={23,12,4,67,20,100,21,45,3,28};
    selectSort(a, 10);
    for (int i=0; i<10; i++) {
        printf("%d\t", a[i]);
    }
    return 0;
}
