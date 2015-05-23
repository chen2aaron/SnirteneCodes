//
//  main.c
//  06-猜数字
//
//  Created by chan on 15/5/23.
//  Copyright (c) 2015年 chan. All rights reserved.
//

#include <stdio.h>
#include <stdlib.h>

int main(int argc, const char * argv[]) {

    //保存产生的随机数
    //获取用户输入的数字
    //保存随机数的新范围
    //保存总次数
    //保存已经猜的次数
    //判断输入数字与电脑产生的数字大小
    int random_num = 0;
    int input_num = 0;
    int total_count = 7;
    int current_count = 1;
    int old_num = 0;
    int flag = 1;
    int m = 1, n = 1000;
    random_num = arc4random_uniform(n-m+1)+m;
    //作弊条
    printf("作弊看看生成的数是多少：\n嘿嘿~是%d~\n",random_num);
    printf("请输入一个[%d~%d]之间的数字\n",m,n);
    while (flag) {
        if (current_count <= total_count) {
            
            scanf("%d",&input_num);
            
            if (input_num < random_num){
                printf("煞笔，猜小了！\n上次竞猜：%d 这次竞猜：%d\n这是第%d次猜了,还有%d次机会了\n",old_num, input_num, current_count, total_count-current_count);
                
            }
            else if (input_num > random_num){
                printf("蠢蛋，猜大了！\n上次竞猜：%d 这次竞猜：%d\n这是第%d次猜了,还有%d次机会了\n",old_num, input_num, current_count, total_count-current_count);
                
            }
            else {
                printf("恭喜啊～猜对了\n");
            }
            old_num = input_num;
            current_count++;
        }
        else {
            printf("智商捉急！你没机会了！\n");
            flag = 0;
            
        }

        
    }
    return 0;
}
