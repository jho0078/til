def sum_of_integers_in_string(foo):
    for i in foo:
        if not i.isdigit():
            foo = foo.replace(i, " ")
            print(foo)


print(sum_of_integers_in_string("The30quick20brown10f0x1203jumps914ov3r1349the102l4zy dog"))

for i in range(1):
    print("a")