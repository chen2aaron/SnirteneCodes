//
//  main.c
//  10-swich点菜
//
//  Created by chan on 15/5/23.
//  Copyright (c) 2015年 chan. All rights reserved.
//

#include <stdio.h>
/*
    为防止case穿透 加break
    default放前面也会穿透
 */
int main(int argc, const char * argv[]) {
    int num = 0;
    printf("本店开张，各种菜品任君挑选，请输入1～7点菜\n");
    scanf("%d",&num);
    if (num >= 1 || num <= 7) {
        switch (num) {
            case 1:
                printf("酱爆乐事");
                break;
            case 2:
                printf("油炸妙脆角");
                break;
            case 3:
                printf("菠萝炒黄瓜");
                break;
            case 4:
                printf("鸡翅烧鸭");
                break;
            case 5:
                printf("油炸开心果");
                break;
            case 6:
                printf("麦片烧鱼");
                break;
            case 7:
                printf("土豆巧克力");
                break;
                
        }
    }
    return 0;
}
