import wsgiref.validate


def get_all_code():  # 用于在界面进行显示
    code = []
    with open("./code/code1.txt") as f:
        for line in f:
            word_list = line.strip().split()
            for i in word_list:
                code.append(i)
    return code


def get_code():  # 二维列表，可以显示行数
    code = []
    with open("./code/code1.txt") as f:
        for line in f:
            word_list = line.strip().split()
            code.append(word_list)
    return code


def go_first(dfa, nfa):     # 去首状态
    for i in dfa:
        if nfa in i['sta']:
            return i['sta']
    print("go_first() is wrong!")
    return 120


def go_next(sta, alp, dfa):
    for i in dfa:
        if len(sta) > 1:
            if sta == i['sta'] and alp == i['alp']:
                return i['next']
    return 120


def in_end(sta):  # 判断该状态是否是终点
    for i in sta:
        if i._end:
            return True
    return False


def whoami(token, word):  # 通过的单词进行分类判定
    if word[0] in token['运算符']:
        return '运算符'
    elif word[0] in token['限定符']:
        return '限定符'
    elif 'a' <= word[0] <= 'z' or word[0] == '_':
        if word in token['关键词']:
            return '关键词'
        else:
            return '标识符'
    elif '0' <= word[0] <= '9':
        return '常量'
    else:
        print("who am i????")
        return -1


def scan(dfa, nfa, token):  # 带入自动机扫描单词
    list_out = []
    code = get_code()
    for i in range(len(code)):
        for one_word in code[i]:
            list_out_row = []
            sta = go_first(dfa, nfa)  # 去第一个状态
            if sta != 120:
                for alp in one_word:
                    sta = go_next(sta, alp, dfa)
                    if sta == 120:
                        break
                if sta != 120 and in_end(sta):  # 扫描成功
                    who = whoami(token, one_word)   # 分类归属
                    token_one = (i + 1, who, one_word)
                    print(token_one)
                    list_out_row = [str(i+1), who, one_word]       # 扫描成功进入列表记录，后续输出成文件用于语法分析
                    list_out.append(list_out_row)
                elif sta == 120:    # 扫描失败
                    token_one = (str(i + 1), "word is wrong!!!", one_word)
                    list_out.append(token_one)
                    print(token_one)
                else:
                    print("啥玩意？？")
    return list_out


def get_states(states):
    sta = ''
    for i in states:
        if isinstance(i, list):
            if sta != '':
                sta = sta + ", " + get_states(i)
            else:
                sta = sta + get_states(i)
        else:
            if sta == '':
                sta = sta + str(i.statenum)
            else:
                sta = sta + ", " + str(i.statenum)
    return sta


def get_nexts(next):
    sta = ''
    for i in next:
        if isinstance(i, list):
            if sta != '':
                sta = sta + ", " + get_nexts(i)
            else:
                sta = sta + get_nexts(i)
        else:
            if sta == '':
                sta = sta + str(i.statenum)
            else:
                sta = sta + ", " + str(i.statenum)
    return sta


def show(dfa):
    print("\n")
    print("\n")
    print("状态转换如下：")
    print("\n")
    a = []
    for i in dfa:
        next = []
        alp = i['alp']
        staa = get_states(i['sta'])  # 得到状态集合
        staa = "{" + staa + "}"
        next = get_nexts(i['next'])
        next = "{" + next + "}"
        b = "state:  " + staa + "          alp:  " + alp + "          next:   " + next
        a.append(b)
        print("state: " + staa + "\t\talp: " + alp + "\t\tnext: " + next)
    with open("./state_changes.txt","w") as f:
        for i in a:
            for j in range(len(i) - 1):
                f.write(i[j])
                f.write(' ')
            f.write(i[-1])
            f.write('\n')