//
//  main.c
//  09-剪刀石头布
//
//  Created by chan on 15/5/23.
//  Copyright (c) 2015年 chan. All rights reserved.
//

#include <stdio.h>
#include <stdlib.h>

int main(int argc, const char * argv[]) {
    /*
     0:剪刀  1:石头  2:布
     计算机出拳：随机生成0 1 2
     人出拳：只能输入0 1 2
     比较计算机和人的出拳
     
     */
    int computer = -1;
    int player = -1;
    computer = arc4random_uniform(3);
    printf("%d\n",computer);
    printf("请出拳，只能输入0，1，2\n0剪刀，1石头，2布\n");
    scanf("%d",&player);
    if (player < 0 ||player > 2){
        printf("请按套路出拳\n");
    }
    else{
        if ((player == 0 && computer == 2)||
            (player == 1 && computer == 0)||
            (player == 2 && computer == 1)) {
            printf("玩家赢\n");
        }
        else if ((computer == 0 && player == 2)||
                 (computer == 1 && player == 0)||
                 (computer == 2 && player == 1)){
            printf("电脑赢\n");}
        else printf("平局\n");
    }
    return 0;
}
