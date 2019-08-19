//
//  ViewController.m
//  Testing-class-dump
//
//  Created by Deloitte Digital on 6/5/2018.
//  Copyright © 2018年 Deloitte-King. All rights reserved.
//

#import "ViewController.h"

#define BUTTON_SIZE 100
#define BUTTON_NAME @"Class-dump"

@interface ViewController ()

@end

@implementation ViewController

- (void)viewDidLoad {
    [super viewDidLoad];
    
    [self addButtonToView:self.view Rect:CGRectMake(100, 100, BUTTON_SIZE, BUTTON_SIZE)];
    [self addButtonToView:self.view Rect:CGRectMake(200, 100, BUTTON_SIZE, BUTTON_SIZE)];
    [self addButtonToView:self.view Rect:CGRectMake(300, 100, BUTTON_SIZE, BUTTON_SIZE)];
    [self addButtonToView:self.view Rect:CGRectMake(100, 200, BUTTON_SIZE, BUTTON_SIZE)];
    [self addButtonToView:self.view Rect:CGRectMake(200, 200, BUTTON_SIZE, BUTTON_SIZE)];
    [self addButtonToView:self.view Rect:CGRectMake(300, 200, BUTTON_SIZE, BUTTON_SIZE)];
    
    NSString *string1 = NSLocalizedString(((NSString *)[NSString stringWithFormat:@"%@", @"AAA"]), nil);
    NSString *string2 = NSLocalizedString(@"HI HI", nil);
    NSLog(@"%@", string2);
    NSLog(@"%@", string1);
    
}

-(void)addButtonToView:(UIView *)view Rect:(CGRect) rect {
    [view addSubview:({
        UIButton *button = [[UIButton alloc] initWithFrame:rect];
        button.backgroundColor = [UIColor blackColor];
        [button setTitle:BUTTON_NAME forState:UIControlStateNormal];
        button;
    })];
}

- (void)didReceiveMemoryWarning {
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}


@end
