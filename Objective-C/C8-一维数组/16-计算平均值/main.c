//
//  main.c
//  16-计算平均值
//
//  Created by chan on 15/5/28.
//  Copyright (c) 2015年 chan. All rights reserved.
//

#include <stdio.h>
// 计算5门课的平均分
float avg(float score[5]){
    float sum = 0.0;
    for (int i=0; i<5; i++) {
        sum += score[i];
    }
    return sum/5;
}
int main(int argc, const char * argv[]) {
    float f1[5]={59.9, 58.43, 60.11, 58.33, 81.66};
    // 数组名作为了函数的实参 地址传递 长度会丢失
    // 不管什么类型的数据，数据的内存地址在内存中占用8个字节
    float av = avg(f1);
    printf("%.2f\n", av);
    return 0;
}
