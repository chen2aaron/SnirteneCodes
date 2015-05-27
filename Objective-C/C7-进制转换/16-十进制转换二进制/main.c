//
//  main.c
//  16-十进制转换二进制
//
//  Created by chan on 15/5/27.
//  Copyright (c) 2015年 chan. All rights reserved.
//

#include <stdio.h>
/**
 *  传递整数n，把n转换成二进制输出
 *  思路分析：&1进行与操作 得到末位
            通过右移获得每一位的末位


 */
void decimalToBinary(n){
    int len = sizeof(n) * 8;
    int temp;
    for (int i=0; i<len; i++) {
        temp = n;
        temp = temp >> (31-i);
        int t = temp & 1;
        printf("%d",t);
    }
    printf("\n");
    
}
int main(int argc, const char * argv[]) {
    decimalToBinary(13);
    return 0;
}
