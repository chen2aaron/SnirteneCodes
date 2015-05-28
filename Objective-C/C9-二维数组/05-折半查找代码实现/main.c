//
//  main.c
//  05-折半查找代码实现
//
//  Created by chan on 15/5/29.
//  Copyright (c) 2015年 chan. All rights reserved.
//

#include <stdio.h>
/**
 *  使用折半查找，来查找一个数的位置
 *
 *  @param arr 数组
 *  @param len 数组长度
 *  @param key 要查找的数
 *
 *  @return 要查找数的位置，如果查找不到返回 -1
 */
int searchItem(int arr[], int len, int key){
    //定义变量
    int low=0,high=len-1,mid;
    //循环
    while (low<=high) {
        //计算mid位置
        mid = (low+high)/2;
        //判断 key和a[mid]
        if (key > arr[mid]) {
            low = mid+1;
        }
        else if(key < arr[mid]){
            high = mid-1;
        }
        else return mid;
    }
    return -1;
}
int main(int argc, const char * argv[]) {
    int a[]={3,4,12,20,21,23,28,45,67,100};
    int location = searchItem(a, 10, 20);
    printf("location = %d\n", location);
    return 0;
}
