#!/usr/bin/env python
# encoding=utf8
# -*- coding: utf-8 -*-
# 本腳本用於對源代碼中的字符串進行解密
# 替換所有加密的char數組為字符串常量，""

import importlib
import os
import re
import sys

#源碼路徑
srcPath = '../Testing-class-dump'

# 替換((char[]){1, 2, 3, 0})的形式為字符串，同時讓每個數組值與0xAA異或進行解密
def replace(match):
    string = match.group(2)
    decodeConfusion_string = ""
    for numberStr in list(string.split(',')):
        if int(numberStr) != 0:
            decodeConfusion_string = decodeConfusion_string + "%c" % (int(numberStr) ^ 0xAA)
    # replaced_string = '\"' + "".join(["%c" % ((int(c) ^ 0xAA) if int(c) != 0 else '\0') for c in string.split(',')]) + '\"'
    replaced_string = '\"' + decodeConfusion_string + '\"'
    # print replaced_string
    print("replaced string = " + replaced_string)
    return '@' + replaced_string


# 修改源代碼，加入字符串加密的函數
def obfuscate(file):
    with open(file, 'r') as f:
        code = f.read()
        f.close()
        code = re.sub(r'(NSSTRING\(|CSTRING\()\(\(char \[\]\) \{(.*?)\}\)(\))', replace, code)
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
            #讀取所有.h和.m 的源文件
            if (extendedName[1] == '.h' or extendedName[1] == '.m'):
                print("处理代码文件:"+ os.path.join(parent,filename))
                obfuscate(os.path.join(parent,filename))

if __name__ == '__main__':
    print("字符串解混淆腳本，將被標記過的char數組轉為字符串，並和0xAA異或。還原代碼")
    if len(srcPath) > 0:
        openSrcFile(srcPath)
    else:
        print("請輸入正確的源代碼路徑")
        sys.exit()
