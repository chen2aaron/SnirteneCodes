//
//  main.c
//  05-游戏方向控制
//
//  Created by chan on 15/5/23.
//  Copyright (c) 2015年 chan. All rights reserved.
//

#include <stdio.h>

int main(int argc, const char * argv[]) {
    // 定义一个死循环
    char direction;
    printf("控制小人方向:w.上 s.下 a.左 d.右 q.退出\n");
    int flag = 1;
    while (flag) {
        scanf("%c",&direction);
        switch (direction) {
            case 'w':
            case 'W':
                printf("上\n");
                break;
            case 'a':
            case 'A':
                printf("左\n");
                break;
            case 's':
            case 'S':
                printf("下\n");
                break;
            case 'd':
            case 'D':
                printf("右\n");
                break;
            case 'q':
            case 'Q':
                printf("程序正在退出....\n");
                printf("程序已经退出\n");
                flag = 0;
                break;
                
            default:
                break;
        }
        
    }
    return 0;
}
