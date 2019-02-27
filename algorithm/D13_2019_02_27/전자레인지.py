# T = int(input())
T = 400

# counta = 0
# countb = 0
# countc = 0
#
# while T >= 300:
#     T -= 300
#     counta += 1
#
# while T >= 60:
#     T -= 60
#     countb += 1
#
# while T >= 10:
#     T -= 10
#     countc += 1
#
# if T == 0:
#     print(counta, countb, countc)
# else:
#     print(-1)

T = 400

a = T//300
T = T%300

b = T//60
T = T%60

c = T//10
T = T%10

if T == 0:
    print(a, b, c)
else:
    print(-1)