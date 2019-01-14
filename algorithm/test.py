def my_all(x):
    for i in x:
        if bool(i) == False:
            return False
    return True

print(my_all([1, 2, 5, '6']))
print(my_all([[], 2, 5, '6']))
print(my_all([]))
print(my_all([0]))

