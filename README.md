# Lexical-analyzer
编译原理课程设计词法分析器

在main.py下方代码中有一个写函数，如果没有该目录会报错，建议注释掉。

项目简介：
词法分析器读入三型文法，将三型文法构建成一个起点和一个终点的NFA，然后将NFA用子集法构造成DFA，创建DFA的索引表，后续读取要扫描的代码，将代码中的每个词依次带入DFA的索引表进行状态转换，如果到达终态说明词符合文法要求，输出token列表（三元组：所在行号，类别，token 内容）如果出错会输出另一种三元组（行号, 对错判定, token内容），并将token列表写入txt文件供任务二LR（1）语法分析器来使用，同时也会将结果输出到result.txt文件来观测，默认注释掉DFA可视化过程，如果想观测状态变化需要把show函数注释取消。

讲解请移步CSDN：https://blog.csdn.net/RLIRiong/article/details/124783174?spm=1001.2014.3001.5501
