## import modules here 

################# Question 0 #################

def add(a, b): # do not change the heading of the function
    return a + b


################# Question 1 #################

def nsqrt(x): # do not change the heading of the function
    a = 0
    b = x
    while (a <= b):
        mid = (a + b) // 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            a = mid + 1
        else:
            b = mid - 1
    return b


################# Question 2 #################


# x_0: initial guess
# EPSILON: stop when abs(x - x_new) < EPSILON
# MAX_ITER: maximum number of iterations

## NOTE: you must use the default values of the above parameters, do not change them

def find_root(f, fprime, x_0=1.0, EPSILON = 1E-7, MAX_ITER = 1000): # do not change the heading of the function
    x = x_0
    for i in range(MAX_ITER):
        x_new = x - f(x)/fprime(x)
        if abs(x - x_new) < EPSILON:
            return x_new
        x = x_new


################# Question 3 #################

class Tree(object):
    def __init__(self, name='ROOT', children=None):
        self.name = name
        self.children = []
        if children is not None:
            for child in children:
                self.add_child(child)
    def __repr__(self):
        return self.name
    def add_child(self, node):
        assert isinstance(node, Tree)
        self.children.append(node)

def make_tree(tokens): # do not change the heading of the function
    if not tokens:
        return
    global stack 
    stack = stack()
    i = 0
    stack.push(tokens[i])
    while i < len(tokens):
        i += 1
        if i == len(tokens):
            break
        if tokens[i] != ']':
            stack.push(tokens[i])
        else:
            item = stack.pop()
            if isinstance(item, Tree) == True:
                M = []
                M.append(item)
                item = stack.pop()
                while item != '[':
                    if isinstance(item, Tree) == True:
                        M.append(item)
                        item = stack.pop()
                    else:
                        t = Tree(item)
                        M.append(t)
                        item = stack.pop()
                item = stack.pop()
                M.reverse()
                t = Tree(item, M)
                stack.push(t)
            else:
                L = []
                while item != '[':
                    if isinstance(item, Tree) == True:
                        L.append(item)
                        item = stack.pop()
                        continue
                    t = Tree(item)
                #L = []
                    L.append(t)
                    item = stack.pop()
                item = stack.pop()
                L.reverse()
                t = Tree(item, L)
                stack.push(t)
    t = stack.pop()
    return t

class stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items)==0

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if not self.isEmpty():
            return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)   

def max_depth(root): # do not change the heading of the function
    if root.children == None:
        return 0
    d = 1
    for child in root.children:
        d = max(d,max_depth(child) + 1)
    return d

L = [[1,2,3]]*4
n = -1
for i in range(4):
    n += 1
    print(L[n][i])