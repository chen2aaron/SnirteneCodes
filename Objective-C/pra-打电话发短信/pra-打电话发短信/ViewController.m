//
//  ViewController.m
//  pra-打电话发短信
//
//  Created by chan on 15/5/19.
//  Copyright (c) 2015年 chan. All rights reserved.
//

#import "ViewController.h"

@interface ViewController ()

@end

@implementation ViewController

- (IBAction)callTo10086:(id)sender {
    NSURL *url = [NSURL URLWithString:@"tel://10086"];
    [[UIApplication sharedApplication] openURL:url];
}
- (IBAction)sendTo10086:(id)sender {
    NSURL *url = [NSURL URLWithString:@"sms://10086"];
    [[UIApplication sharedApplication] openURL:url];
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
