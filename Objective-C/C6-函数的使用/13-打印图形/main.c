//
//  main.c
//  13-打印图形
//
//  Created by chan on 15/5/24.
//  Copyright (c) 2015年 chan. All rights reserved.
//

#include <stdio.h>

int main(int argc, const char * argv[]) {
    int print_nline(int n);
    print_nline(6);
    return 0;
}

void print_line(){
    printf("---------------\n");
}

int print_nline(int n){
    for (int i=0; i<n; i++) {
        print_line();
    }
    return 0;
}