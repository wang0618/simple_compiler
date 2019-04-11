## C语言和Simple+语言(一个自定义的类Pascl语言)的语法分析器


### 本语法分析器实现的功能
本程序使用Python编码实现，词法分析采用了沿用了作业一的代码，语法分析实现的功能有：
 - 利用文法推导式构造LR(1)分析表
 - 使用LR(1)分析表对输入的Token串进行语法分析，构建语法树
 - 在构建语法树的时候进行一些标识符类型的识别
 - 树形输出语法树，可视化输出语法树构建过程
 - 词法语法检错，显示出错代码上下文和出错原因

### 程序运行结果

在控制台进入项目目录，使用以下几条命令运行程序
1. `python3 main.py src_path [show-tree-animation] [show-simplify-tree]`
2. `python3 main.py make-parse-table`
3. `python3 main_c.py c_src_path`

命令2用来构造语言的LR(1)语法分析表，并将分析表以文件的形式保存到项目目录的`data`文件夹中；
命令1用来对输入路径为`src_path`的源文件进行语法分析，选项`show-tree-animation`用于开启可视化输出语法树构建过程，选项`show-simplify-tree`设置输出简化版的语法树
命令3可以对C语言源程序进行语法分析并生成语法分析树，但程序词法分析所接受的Token为标准C语言的子集(比如不支持读入`5e-5`形式的浮点数)

下面为语法分析器对以下源程序进行语法分析的结果
```pascal
program sample
constant 
    pi=3.1415926;
    e=2.71828182;
var 
    a : array[2] of integer;
    b : integer;
procedure show(a:char) begin
	call writeln(a)
end
begin
    a[0] := 1;
    a[1] := pi + 1;
    b := e * 100;
    if a or b then
		call writeln('a or b is true')
	else
		call writeln('all false')
end
```
程序语法树构造结果截图(原始图片见附件)：
![Alt text](./simple_parse_tree.png)

加入`show-tree-animation`选项开启动画效果输出的程序运行过程:
[![asciicast](https://asciinema.org/a/9PJfaMi7TqzxgjkGiI9opkldB.svg)](https://asciinema.org/a/9PJfaMi7TqzxgjkGiI9opkldB)

经过符号类型识别后符号表的内容：
![Alt text](./doc/assets/3.png)

源文件存在词法错误时的输出：
![Alt text](./doc/assets/4.png)

源文件存在语法错误时的输出：
![Alt text](./doc/assets/5.png)

以下为程序对项目下二分搜索C程序`binary_search.c`进行语法分析所得的语法树(原始图片见附件)：
![Alt text](./c_parse_tree_simplified.png)
