s = []

def check_matching(item):
    for i in item:
        if i == '(':
            s.append(item)
        else:
            if len(s) == 0:
                return False
            s.pop(-1)

    if len(s) != 0:
        return False
    else:
        return True

print(check_matching('()()((()))'))
print(check_matching('()()((())))'))
print(check_matching('((()((((()()((()())((())))))'))


