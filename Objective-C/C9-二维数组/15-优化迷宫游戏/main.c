//
//  main.c
//  14-迷宫游戏
//
//  Created by chan on 15/5/29.
//  Copyright (c) 2015年 chan. All rights reserved.
//
/**
 *  游戏说明:玩家通过键盘录入w,s,a,d控制小人向不同方向移动,当小人移动到出口位置,玩家胜利
 
 */
#include <stdio.h>
#define ROW 6
#define COL 12
/**
 *  打印地图
 *
 *  @param arr 地图数组
 */
void printMap(char map[ROW][COL]){
    for (int i=0; i<ROW; i++) {
        for (int j=0; j<COL; j++) {
            printf("%c",map[i][j]);
        }
        printf("\n");
    }
}
/**
 *  实现小人移动
 *
 *  @param map  地图数组
 *  @param oldX 小人原始X坐标
 *  @param oldY 小人原始Y坐标
 *  @param newX 小人现在X坐标
 *  @param newY 小人现在Y坐标
 */
void personMove(char map[ROW][COL], int oldX,int oldY,int newX, int newY){
    char temp;
    temp = map[oldX][oldY];
    map[oldX][oldY] = map[newX][newY];
    map[newX][newY] = temp;
}
int main(int argc, const char * argv[]) {
    //    定义变量
    //    1.地图, 方向, 小人位置
    char map[ROW][COL]={
        {'#','#','#','#','#','#','#','#','#','#','#','#'},
        {'#','O','#','#',' ',' ','#',' ',' ',' ','#','#'},
        {'#',' ','#','#',' ','#','#',' ','#',' ','#','#'},
        {'#',' ',' ','#',' ',' ',' ',' ','#',' ',' ',' '},
        {'#','#',' ',' ',' ','#','#','#',' ',' ','#','#'},
        {'#','#','#','#','#','#','#','#','#','#','#','#'},
    };
    char direction;
    int currentX = 1;
    int currentY = 1;
    char street = ' ';
    //    2.先打印地图
    printMap(map);
    //    3.提示用户玩法
    printf("请控制小人移动：w.上 s.下 a.左 d.右 q.退出\n");
    //    循环控制
    //    4.接受用户输入的方向
    //    5.判断用户驶入了什么方向
    //    判断小人能否移动
    //    6.判断小人能否移动,小人的下一个位置是否是路
    //    if 是 交换小人与路的位置
    //        重新记录小人的位置
    //        else 否 什么也不干
    //            判断是否走出来
    //            7.判断y的值是否==5
    //            提示走出迷宫
    //            break 游戏结束
    int flag = 1;
    while (flag) {
        scanf("%c",&direction);
        getchar(); //吸收换行符 \n
        switch (direction) {
            case 'w':
            case 'W':
                if (map[currentX-1][currentY]==street) {
                    personMove(map, currentX, currentY, currentX-1, currentY);
                    currentX--;
                }
                break;
            case 's':
            case 'S':
                if (map[currentX+1][currentY]==street) {
                    personMove(map, currentX, currentY, currentX+1, currentY);
                    currentX++;
                }
                break;
            case 'a':
            case 'A':
                if (map[currentX][currentY-1]==street) {
                    personMove(map, currentX, currentY, currentX, currentY-1);
                    currentY--;
                }
                break;
            case 'd':
            case 'D':
                if (map[currentX][currentY+1]==street) {
                    personMove(map, currentX, currentY, currentX, currentY+1);
                    currentY++;
                }
                break;
            case 'q':
            case 'Q':
                printf("程序正在退出....\n");
                printf("程序已经退出\n");
                flag = 0;
                break;
        }
        printMap(map);
        if (currentY==COL-1) {
            printf("恭喜！你走出了迷宫~\n");
            break;
        }
        
    }
    
    return 0;
}
