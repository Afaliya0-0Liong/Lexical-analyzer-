statenum = 0


class state:
    def __init__(self, _end, statenum, list_source_one, is_right):
        self._end = _end  # 是否是产生式的终点
        self.notepsilon = {}  # 路径非空的字典，方便后续查找
        self.epsilon = []  # 路径为空的列表
        self.statenum = statenum
        if is_right:
            if len(list_source_one[1]) > 1:
                self.right = list_source_one[1][1]  # 保存右部非终结符
            else:
                self.right = ' '
        else:
            self.left = list_source_one[0]  # 保存左部非终结符

    def set_end(self, _end):
        self._end = _end


def add_epsilon_road(begin, end):  # 添加空路径
    begin.epsilon.append(end)


def add_road(begin, end, a):  # 添加非空路径
    begin.notepsilon[a] = end


def one_road(list_source):  # A -> aB    或者 A -> a
    global statenum
    begin = state(False, statenum, list_source, False)
    end = state(True, statenum + 1, list_source, True)
    add_road(begin, end, list_source[1][0])  # 添加路径
    statenum += 2
    return begin, end


def more_road(list_source):  # A -> aA   两条路径
    global statenum
    begin = state(False, statenum, list_source, False)
    end = state(True, statenum + 1, list_source, True)
    add_road(begin, end, list_source[1][0])
    add_epsilon_road(end, begin)
    statenum += 2
    return begin, end


def union(tuple1, tuple2):
    global statenum
    begin = state(False, statenum, [' ', ' '], False)
    end = state(True, statenum + 1, [' ', ' '], True)
    add_epsilon_road(begin, tuple1[0])
    add_epsilon_road(begin, tuple2[0])
    add_epsilon_road(tuple1[1], end)
    add_epsilon_road(tuple2[1], end)
    tuple1[1].set_end(False)        # 改为非终点
    tuple2[1].set_end(False)
    statenum += 2
    return begin, end


def go_nfa(list_source):
    global statenum
    stack = []
    start_stack = []  # 用来合并状态，只有包括起始状态的元组才可以进行合并    其他会由这些状态延伸到终态
    end_stack = []  # 终结状态会指向最终状态
    s = list_source[0][0]
    for i in range(len(list_source)):
        tuple1 = ()
        if len(list_source[i][1]) == 1 or (len(list_source[i][1]) > 1 and list_source[i][0] != list_source[i][1][1]):
            tuple1 = one_road(list_source[i])
            stack.append(tuple1)
            if s == list_source[i][0]:
                start_stack.append(tuple1)
            if len(list_source[i][1]) == 1:
                end_stack.append(tuple1)
        else:
            tuple1 = more_road(list_source[i])
            stack.append(tuple1)  # 至此创建了多个分散的NFA，存在stack中
            if s == list_source[i][0]:
                start_stack.append(tuple1)
    for i in stack:
        for j in stack:
            if i[1].right != ' ' and i[1].right == j[0].left and i != j:
                add_epsilon_road(i[1], j[0])
    while len(start_stack) > 1:
        tuple1 = start_stack.pop()
        tuple2 = start_stack.pop()  # 提取两个独立以起点为开始的NFA进行合并
        start_stack.append(union(tuple1, tuple2))
    for i in end_stack:
        if i[0].left != s:
            add_epsilon_road(i[1], start_stack[0][1])  # A -> a类(不包含首状态)的结尾和最终结尾接线
    return start_stack.pop()
