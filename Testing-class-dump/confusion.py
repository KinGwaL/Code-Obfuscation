#!/usr/bin/env python
# encoding=utf8
# -*- coding: utf-8 -*-
# 本腳本用於對源代碼中的字符串進行加密
# 替換所有字符串常量為加密的char數組，形式((char[]){1, 2, 3, 0})

import importlib
import os
import re
import sys

#源碼路徑
srcPath = '../Testing-class-dump'

# 插入宏和解密函數，解密方法：每個字節與0xAA異或
insert_code = '''#define STRING_OBFUSCATE
    
    static char* decryptConstString(char* string) __attribute__((always_inline));
    
    #define NSSTRING(string) [NSString stringWithUTF8String:decryptConstString(string)]
    #define CSTRING(string) decryptConstString(string)
    
    static char* decryptConstString(char* string)
    {
    char* origin_string = string;
    while(*string) {
    *string ^= 0xAA;
    string++;
    }
    return origin_string;
    }
    
    #ifndef STRING_OBFUSCATE'''

# 替換字符串為((char[]){1, 2, 3, 0})的形式，同時讓每個字節與0xAA異或進行加密
def replace(match):
    # print string
    print("pre-relace string = " + match.group(2))
    
    string = match.group(2) + '\x00'
    
    replaced_string = '((char []) {' + ', '.join(["%i" % ((ord(c) ^ 0xAA) if c != '\0' else 0) for c in list(string)]) + '})'

    return match.group(1) + 'NSSTRING(' + replaced_string + ')'

# 修改源代碼，加入字符串加密的函數
def obfuscate(file):
    with open(file, 'r') as f:
        code = f.read()
        f.close()
        code = re.sub(r'(NSLocalizedString\()@"(.*?)"', replace, code)
        #code = re.sub(r'(NSSTRING\(|CSTRING\()"(.*?)"(\))', replace, code)
        #code = code.replace('#ifndef STRING_OBFUSCATE', insert_code)
        # print code
        with open(file, 'w') as f:
            f.write(code)
            f.close()

#讀取源碼路徑下的所有.h和.m 文件
def openSrcFile(path):    
    print("開始處理路徑："+ path +" 下的所有.h和.m文件")
    # this folder is custom
    for parent,dirnames,filenames in os.walk(path):
        #case 1:
#        for dirname in dirnames:
#            print((" parent folder is:" + parent).encode('utf-8'))
#            print((" dirname is:" + dirname).encode('utf-8'))
        #case 2
        for filename in filenames:
            extendedName = os.path.splitext(os.path.join(parent,filename))
            if (extendedName[1] == '.h' or extendedName[1] == '.m'):
                print("處理源代碼文件: "+ os.path.join(parent,filename))
                obfuscate(os.path.join(parent,filename))

if __name__ == '__main__':
    print("本腳本用於對源代碼中被標記的字符串進行加密")

    if len(srcPath) > 0:
        openSrcFile(srcPath)
    else:
        print("請輸入正確的源代碼路徑")
        sys.exit()
