//
//  main.c
//  04-逆序排序
//
//  Created by chan on 15/5/31.
//  Copyright (c) 2015年 chan. All rights reserved.
//

#include <stdio.h>
void reverseArray(int arr[], int len){
    int *p = arr;
    unsigned i = 0;
    unsigned j = len-1;
    int temp;
    while (i<j) {

        temp = *(p+i);
        *(p+i) = *(p+j);
        *(p+j) = temp;
        i++, j--;
    }
}


int main(int argc, const char * argv[]) {
    int arr[10] = {1,2,3,4,5,6,7,8,9,10};
    reverseArray(arr, sizeof(arr)/sizeof(int));
    for (int i=0; i<10; i++) {
        printf("%d ", arr[i]);
    }
    return 0;
}
