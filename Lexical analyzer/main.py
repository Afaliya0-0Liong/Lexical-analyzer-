import to_nfa
import to_dfa
import read
keywords = ['include', 'iostream', 'using', 'namespace', 'std', 'main', 'int', 'const',  'double', 'return']
delimiter = [';', '#', '<', '>', '(', ')', '{', '}']
constant = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
operator = ['+', '-', '*', '/', '=']
identifier = ['_', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
token = {'关键词': keywords, '限定符': delimiter, '常量': constant, '运算符': operator, '标识符': identifier }
# token表


def main():
    file = open("./expression/ex1.txt", encoding="utf-8")
    list_row = file.readlines()
    list_source = []
    for i in range(len(list_row)):
        list_col = list_row[i].strip().split('->')
        list_source.append(list_col)
    file.close()
    alphabet = []       # 终结符表，用于后续索引
    for i in range(len(list_source)):
        if list_source[i][1][0] not in alphabet:
            alphabet.append(list_source[i][1][0])
    nfa = to_nfa.go_nfa(list_source)        # 转换为nfa元组（起点,终点）
    dfa = to_dfa.go_dfa(nfa, alphabet)      # 转换为dfa元组（dfa表, 起点）
    all_code = read.get_all_code()
    print("需要扫描的词： ")
    print(all_code)
    print("三元组格式：")
    print("（行号, token类别, 具体内容）")
    print("或者： ")
    print("（行号, 对错判定, 具体内容）")
    list_out = read.scan(dfa[0], nfa[0], token)        # 扫描并输出token列表,返回值用来写入文件
    with open("../Parser/code/out_from_task1.txt", "w") as f:   # 用于任务二
        for i in list_out:
            for j in range(len(i) - 1):
                f.write(i[j])
                f.write(' ')
            f.write(i[-1])
            f.write('\n')
    with open("./result.txt", "w") as f:   # 用于输出在项目文件中，用于exe文件的使用
        for i in list_out:
            for j in range(len(i) - 1):
                f.write(i[j])
                f.write(' ')
            f.write(i[-1])
            f.write('\n')
    # read.show(dfa[0])                     # 可以通过该方法进行可视化，查看dfa的状态转换


if __name__ == "__main__":
    main()
