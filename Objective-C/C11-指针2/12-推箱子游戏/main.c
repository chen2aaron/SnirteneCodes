//
//  main.c
//  12-推箱子游戏
//
//  Created by chan on 15/5/31.
//  Copyright (c) 2015年 chan. All rights reserved.
//

#include <stdio.h>
#define kRows 10
#define kCols 17
/**
 *  重点：
    1.小人在移动的时候，如何判断旁边是箱子
    2.小人推箱子的时候，箱子要移动的下个位置是路
    3.记录小人的位置和下一个位置，箱子的位置和下一个位置
    4.计算箱子的下一个位置
    5.地图
 */
/**
 *  伪代码：
    1.定义变量
        地图
        小人 旧位置 新位置
        箱子 旧位置 新位置
        用户输入方向
    2.打印地图
 
    3.循环控制程序
        接受用户输入的方向
        判断方向
    4.判断模块
        根据方向判断如何移动
            是路 小人移动
            不是路 
                是箱子 计算箱子下一个位置
                    箱子下一个位置是是路 移动小人和箱子
                        a.箱子移动到下一个位置
                        b.小人移动到箱子原来的位置
                不是箱子  就是墙 什么也不干
 
    5.刷新地图
 
    6.判断是否走出来
        箱子的位置==出口的位置
 */

void printMap(char map[kRows][kCols]){
    for (int i=0; i<kRows; i++) {
        printf("%s\n", map[i]);
    }
}

void move1(char map[kRows][kCols], int oldX, int oldY, int newX, int newY){
    char temp;
    temp = map[oldX][oldY];
    map[oldX][oldY] = map[newX][newY];
    map[newX][newY] = temp;
}
int main(int argc, const char * argv[]) {
    //     1.定义变量
    //         地图
    char map[kRows][kCols]={
        "################",
        "#O ##       #  #",
        "# X## ### ###  #",
        "#           #  #",
        "#  ##  ###     #",
        "####  ####  #  #",
        "###    ##  ##  #",
        "### # ##  ###  #",
        "##              ",
        "################",
    };
    //         小人 旧位置 新位置
    int personNowX = 1;
    int personNowY = 1;
    int personNextX = personNowX;
    int personNextY = personNowY;
    //         箱子 旧位置 新位置
    int boxNowX = 2;
    int boxNowY = 2;
    int boxNextX = boxNowX;
    int boxNextY = boxNowY;
    char box = 'X';
    //         用户输入方向
    char direction;
    //         路
    char street = ' ';
    //     2.打印地图
    printMap(map);
    printf("请安wsad控制小人移动，按q退出\n");
    
    //     3.循环控制程序
    while (1) {
        //         接受用户输入的方向
        scanf("%c", &direction);
        getchar();
        //        防止穿墙
        personNextX = personNowX;
        personNextY = personNowY;
        //         判断方向
        switch (direction) {
            case 'w':
            case 'W':
                personNextX--;
                break;
            case 's':
            case 'S':
                personNextX++;
                break;
            case 'a':
            case 'A':
                personNextY--;
                break;
            case 'd':
            case 'D':
                personNextY++;
                break;
            case 'q':
            case 'Q':
                printf("程序正在退出....\n");
                printf("程序已经退出\n");
                return 0;
                break;
        }
        
        //     4.判断模块
        //         根据方向判断如何移动
        if (map[personNextX][personNextY]==street) {
            
            
            //             是路 小人移动
            move1(map, personNowX, personNowY, personNextX, personNextY);
            personNowX = personNextX;
            personNowY = personNextY;
        }
        else if (map[personNextX][personNextY]==box){
            
            //             不是路
            //                 是箱子 计算箱子下一个位置
            boxNextX = boxNowX+(boxNowX-personNowX);
            boxNextY = boxNowY+(boxNowY-personNowY);
            if (map[boxNextX][boxNextY]==street) {
                //                     箱子下一个位置是是路 移动小人和箱子
                //                         a.箱子移动到下一个位置
                move1(map, boxNowX, boxNowY, boxNextX, boxNextY);
                //                         b.小人移动到箱子原来的位置
                move1(map, personNowX, personNowY, boxNowX, boxNowY);
                //            调整小人和箱子的位置
                personNowX = personNextX;
                personNowY = personNextY;
                boxNowX = boxNextX;
                boxNowY = boxNextY;
                
            }
            //                 不是箱子  就是墙 什么也不干
            //
            
        }
        //     5.刷新地图
        printMap(map);
        //     6.判断是否走出来
        //         箱子的位置==出口的位置
        if (boxNowY == kCols-2) {
            printf("恭喜走出来了～\n");
            break;
        }
    }
    return 0;
}
