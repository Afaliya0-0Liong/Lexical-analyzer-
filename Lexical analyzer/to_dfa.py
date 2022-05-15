gura = []


def get_same_state(begin, ahead_state):  # 深度搜索策略寻找可以直达的状态
    if len(begin.epsilon) > 0:
        for i in begin.epsilon:
            if i not in ahead_state:
                ahead_state.append(i)
                get_same_state(i, ahead_state)


def go_circle(same_state, visit_state):  # 判断是否完成遍历等价状态
    global gura
    for i in same_state:
        if i not in visit_state:
            visit_state.append(i)
            gura = i
            return True
    return False


def get_next_state(gura, alp, next_state):  # 得到等价状态通过某一个非终结符到的下一个非空状态集
    for i in gura:
        if len(i.notepsilon) > 0:
            if alp == list(i.notepsilon.keys())[0]:
                next_state.append(i.notepsilon[alp])


def go_dfa(nfa, alphabet):
    global gura
    ahead_state = []  # 等价状态集
    same_state = []  # 等价状态集的列表(epsilon可以访问)
    visit_state = []  # 访问过等价状态集
    next_state = []  # 等价状态下的下一个非空状态集
    form = []  # 最后的查询表

    ahead_state.append(nfa[0])
    get_same_state(nfa[0], ahead_state)
    same_state.append(ahead_state)
    while go_circle(same_state, visit_state):  # 依次遍历等价状态集
        for i in alphabet:
            ahead_state = []
            next_state = []
            get_next_state(gura, i, next_state)  # 得到等价状态通过某一个非终结符到的下一个非空状态集
            # print(next_state)
            for j in next_state:
                ahead_state.append(j)  # 将非空小状态挨个依次存入等价状态集，下面开始找等价空状态
                get_same_state(j, ahead_state)  # 寻找输入了某一个终结符之后所有可以直达的状态集
            if ahead_state not in same_state and len(ahead_state) > 0:
                same_state.append(ahead_state)
            colu = {'sta': gura, 'alp': i, 'next': ahead_state}
            if colu['next']:
                form.append(colu)
    return form, nfa[0]
