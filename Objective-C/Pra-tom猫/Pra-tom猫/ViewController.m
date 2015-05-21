//
//  ViewController.m
//  Pra-tom猫
//
//  Created by chan on 15/5/19.
//  Copyright (c) 2015年 chan. All rights reserved.
//

#import "ViewController.h"

@interface ViewController ()
@property (weak, nonatomic) IBOutlet UIImageView *tomImgView;

@end

@implementation ViewController
- (IBAction)knockTOM:(id)sender {
    // 图片集合
    NSMutableArray *imgs = [[NSMutableArray alloc] init];
    
    // 遍历图片
    for(int i=0;i<81;i++){
        NSString *imgName = [NSString stringWithFormat:@"cat_knockout%04d.jpg",i];
        // 获取图片对象
        UIImage *img = [UIImage imageNamed:imgName];
        
        // 存到集合中
        [imgs addObject:img];
    }
    // 给图片设定动画
    _tomImgView.animationImages = imgs;
    
    // 设定动画时长
    _tomImgView.animationDuration = imgs.count * 0.05;
    
    // 重复次数
    _tomImgView.animationRepeatCount = 1;
    
    // 播放动画
    [_tomImgView startAnimating ];
}

- (void)viewDidLoad {
    [super viewDidLoad];
    // Do any additional setup after loading the view, typically from a nib.
}

- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

@end
