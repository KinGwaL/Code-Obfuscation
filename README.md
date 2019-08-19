# Code-Obfuscation

# What is this?
This image is talking about the function calling flow will display the function full name when you are using some hooking tools like class-dump, Hopper to check your application which is not secure.\
![alt text](https://raw.githubusercontent.com/KinGwaL/Code-Obfuscation/master/images/image1.png)

Below image is the final result after code obfuscation and the document will teach you how to do this.\
![alt text](https://raw.githubusercontent.com/KinGwaL/Code-Obfuscation/master/images/image2.png)
 
# User guide
1.  Create a directory call “Resource” into your project.\
![alt text](https://raw.githubusercontent.com/KinGwaL/Code-Obfuscation/master/images/image3.png)
2.	Copy all file into Resource. (symbols will generate automatically.)\
![alt text](https://raw.githubusercontent.com/KinGwaL/Code-Obfuscation/master/images/image4.png)
3.	Go to “Build Phases”, click “+” then “New Run Script Phase”, and add the script like below.\
![alt text](https://raw.githubusercontent.com/KinGwaL/Code-Obfuscation/master/images/image5.png)\
![alt text](https://raw.githubusercontent.com/KinGwaL/Code-Obfuscation/master/images/image6.png)\
4.	Go to “Build Settings” and input the related details like below image. Make sure you have change “Precompile Prefix Header” to Yes.\
![alt text](https://raw.githubusercontent.com/KinGwaL/Code-Obfuscation/master/images/image7.png)
5.	Go to your confuse.sh directory using terminal, change file permission by chmod.\
![alt text](https://raw.githubusercontent.com/KinGwaL/Code-Obfuscation/master/images/image8.png)
6.	For example, there have a function call “addButtonToView”, we can put this string into func.list, then run your project.\
![alt text](https://raw.githubusercontent.com/KinGwaL/Code-Obfuscation/master/images/image9.png)
![alt text](https://raw.githubusercontent.com/KinGwaL/Code-Obfuscation/master/images/image10.png)\
codeObfuscation.h file will generate a define object related your requirement.\
![alt text](https://raw.githubusercontent.com/KinGwaL/Code-Obfuscation/master/images/image11.png)

prefunc.list will display the full function list according to your project, you can paste these strings to fune.list by consider the roles as below:
1.	Not system method / parameter, such as view, viewDidLoad
2.	Not XIB drag line control name

 
# Reference
1.	https://blog.csdn.net/yiyaaixuexi/article/details/29201699
2.	https://www.jianshu.com/p/19bf42f22473

